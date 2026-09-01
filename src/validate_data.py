"""Validate the raw Hillstrom email experiment file without modifying it."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import chisquare, chi2_contingency


EXPECTED_COLUMNS = [
    "recency",
    "history_segment",
    "history",
    "mens",
    "womens",
    "zip_code",
    "newbie",
    "channel",
    "segment",
    "visit",
    "conversion",
    "spend",
]

EXPECTED_ARMS = {"No E-Mail", "Mens E-Mail", "Womens E-Mail"}
BINARY_COLUMNS = ["mens", "womens", "newbie", "visit", "conversion"]


def validate(path: Path) -> dict:
    df = pd.read_csv(path)
    if list(df.columns) != EXPECTED_COLUMNS:
        raise ValueError(f"Unexpected columns: {list(df.columns)}")
    if set(df["segment"].unique()) != EXPECTED_ARMS:
        raise ValueError(f"Unexpected experiment arms: {df['segment'].unique().tolist()}")

    invalid_binary_rows = int((~df[BINARY_COLUMNS].isin([0, 1])).any(axis=1).sum())
    arm_counts = df["segment"].value_counts().sort_index()
    srm_statistic, srm_p_value = chisquare(arm_counts.to_numpy())

    numeric_balance = {}
    for column in ["recency", "history", "mens", "womens", "newbie"]:
        means = df.groupby("segment", observed=True)[column].mean()
        standardized_span = float((means.max() - means.min()) / df[column].std(ddof=1))
        numeric_balance[column] = {
            "arm_means": {key: float(value) for key, value in means.items()},
            "max_standardized_mean_difference": standardized_span,
        }

    categorical_balance = {}
    for column in ["history_segment", "zip_code", "channel"]:
        table = pd.crosstab(df[column], df["segment"])
        statistic, p_value, _, _ = chi2_contingency(table)
        n = int(table.to_numpy().sum())
        degrees = min(table.shape) - 1
        cramers_v = float(np.sqrt(statistic / (n * degrees)))
        categorical_balance[column] = {
            "chi_square": float(statistic),
            "p_value": float(p_value),
            "cramers_v": cramers_v,
        }

    return {
        "path": str(path),
        "rows": int(len(df)),
        "columns": int(df.shape[1]),
        "missing_cells": int(df.isna().sum().sum()),
        "identical_observed_rows": int(df.duplicated().sum()),
        "invalid_binary_rows": invalid_binary_rows,
        "conversion_without_visit": int(((df["conversion"] == 1) & (df["visit"] == 0)).sum()),
        "positive_spend_without_conversion": int(((df["spend"] > 0) & (df["conversion"] == 0)).sum()),
        "conversion_with_zero_spend": int(((df["conversion"] == 1) & (df["spend"] <= 0)).sum()),
        "negative_history": int((df["history"] < 0).sum()),
        "negative_spend": int((df["spend"] < 0).sum()),
        "arm_counts": {key: int(value) for key, value in arm_counts.items()},
        "sample_ratio_test": {
            "chi_square": float(srm_statistic),
            "p_value": float(srm_p_value),
        },
        "numeric_balance": numeric_balance,
        "categorical_balance": categorical_balance,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(validate(args.data), indent=2))


if __name__ == "__main__":
    main()

