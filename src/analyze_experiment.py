"""Produce transparent preliminary intent-to-treat experiment estimates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats


CONTROL = "No E-Mail"
CONTRASTS = [
    ("Mens E-Mail", CONTROL, "confirmatory"),
    ("Womens E-Mail", CONTROL, "confirmatory"),
    ("Mens E-Mail", "Womens E-Mail", "exploratory"),
]


def wilson_interval(successes: int, observations: int, alpha: float = 0.05) -> tuple[float, float]:
    """Wilson score interval for one binomial proportion."""
    proportion = successes / observations
    z_value = stats.norm.ppf(1 - alpha / 2)
    denominator = 1 + z_value**2 / observations
    center = (proportion + z_value**2 / (2 * observations)) / denominator
    half_width = (
        z_value
        * np.sqrt(proportion * (1 - proportion) / observations + z_value**2 / (4 * observations**2))
        / denominator
    )
    return center - half_width, center + half_width


def holm_adjust(p_values: list[float]) -> list[float]:
    """Return Holm step-down adjusted p-values in their original order."""
    values = np.asarray(p_values, dtype=float)
    order = np.argsort(values)
    adjusted = np.empty_like(values)
    running_maximum = 0.0
    total = len(values)
    for rank, position in enumerate(order):
        candidate = min(1.0, (total - rank) * values[position])
        running_maximum = max(running_maximum, candidate)
        adjusted[position] = running_maximum
    return adjusted.tolist()


def proportion_difference(a: pd.DataFrame, b: pd.DataFrame, outcome: str) -> dict:
    x_a, n_a = int(a[outcome].sum()), len(a)
    x_b, n_b = int(b[outcome].sum()), len(b)
    p_a, p_b = x_a / n_a, x_b / n_b
    pooled = (x_a + x_b) / (n_a + n_b)
    null_se = np.sqrt(pooled * (1 - pooled) * (1 / n_a + 1 / n_b))
    z_score = (p_a - p_b) / null_se
    p_value = float(2 * stats.norm.sf(abs(z_score)))
    difference = p_a - p_b
    lower_a, upper_a = wilson_interval(x_a, n_a)
    lower_b, upper_b = wilson_interval(x_b, n_b)
    return {
        "treatment_rate": p_a,
        "comparison_rate": p_b,
        "absolute_difference": difference,
        "relative_lift": p_a / p_b - 1,
        "ci_95_newcombe": [lower_a - upper_b, upper_a - lower_b],
        "p_value_unadjusted": p_value,
    }


def mean_difference(a: pd.DataFrame, b: pd.DataFrame) -> dict:
    test = stats.ttest_ind(a["spend"], b["spend"], equal_var=False)
    difference = float(a["spend"].mean() - b["spend"].mean())
    variance_a = float(a["spend"].var(ddof=1))
    variance_b = float(b["spend"].var(ddof=1))
    se = np.sqrt(variance_a / len(a) + variance_b / len(b))
    numerator = (variance_a / len(a) + variance_b / len(b)) ** 2
    denominator = (variance_a / len(a)) ** 2 / (len(a) - 1) + (variance_b / len(b)) ** 2 / (len(b) - 1)
    degrees_freedom = numerator / denominator
    critical = stats.t.ppf(0.975, degrees_freedom)
    return {
        "treatment_mean": float(a["spend"].mean()),
        "comparison_mean": float(b["spend"].mean()),
        "absolute_difference": difference,
        "relative_lift": difference / float(b["spend"].mean()),
        "ci_95_welch": [difference - critical * se, difference + critical * se],
        "p_value_unadjusted": float(test.pvalue),
    }


def analyze(path: Path) -> dict:
    df = pd.read_csv(path)
    arm_metrics = (
        df.groupby("segment", observed=True)
        .agg(
            n=("segment", "size"),
            visits=("visit", "sum"),
            visit_rate=("visit", "mean"),
            conversions=("conversion", "sum"),
            conversion_rate=("conversion", "mean"),
            total_revenue=("spend", "sum"),
            revenue_per_customer=("spend", "mean"),
        )
        .sort_index()
    )

    contrasts = []
    for treatment, comparison, status in CONTRASTS:
        a = df[df["segment"] == treatment]
        b = df[df["segment"] == comparison]
        contrasts.append(
            {
                "treatment": treatment,
                "comparison": comparison,
                "status": status,
                "visit": proportion_difference(a, b, "visit"),
                "conversion": proportion_difference(a, b, "conversion"),
                "spend": mean_difference(a, b),
            }
        )

    confirmatory = [item for item in contrasts if item["status"] == "confirmatory"]
    for outcome in ["visit", "conversion", "spend"]:
        adjusted = holm_adjust([item[outcome]["p_value_unadjusted"] for item in confirmatory])
        for item, p_value in zip(confirmatory, adjusted):
            item[outcome]["p_value_holm"] = p_value

    return {
        "arm_metrics": arm_metrics.reset_index().to_dict(orient="records"),
        "contrasts": contrasts,
        "warning": "Revenue intervals are preliminary Welch checks; add bootstrap and randomization inference before final reporting.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(analyze(args.data), indent=2))


if __name__ == "__main__":
    main()
