# AI_augmented_retail-email-abn-testing-
Initialize A/B/n testing project structure and analysis plan
# Retail Email Experiment: A/B/n Testing, Incrementality, and Targeting

An end-to-end analysis of a randomized three-arm retail email experiment. The project is organized around a management decision:

> Should the retailer send a promotional email, which creative should it use, and how much incremental revenue can it reasonably expect?

## Why this project matters

This is not a synthetic two-row-rate exercise. The source data contains 64,000 customers randomly assigned to:

- no email (control),
- a men's merchandise email, or
- a women's merchandise email.

Customer visits, conversions, and spend were observed for two weeks after assignment. The analysis demonstrates experiment validation, intent-to-treat estimation, uncertainty, multiple-comparison control, power analysis, and responsible segment exploration.

## Current status

**Phase 1: dataset audit and analysis design — complete.**

The initial audit found:

| Check | Result |
|---|---:|
| Rows | 64,000 |
| Columns | 12 |
| Missing values | 0 |
| Invalid binary values | 0 |
| Conversions without a visit | 0 |
| Positive spend without conversion | 0 |
| Sample-ratio mismatch test | chi-square = 0.203; p = 0.904 |
| Largest standardized mean difference across numeric covariates | 0.009 |

The 6,562 fully repeated rows must **not** be automatically deleted. The source has no customer identifier, and repeated low-information records can represent different customers with the same observed values.

## Preliminary arm metrics

These figures are descriptive and are included to orient the analysis. Final claims will use prespecified estimands, confidence intervals, robust inference, and multiplicity control.

| Arm | N | Visit rate | Conversion rate | Revenue/customer |
|---|---:|---:|---:|---:|
| No email | 21,306 | 10.62% | 0.57% | $0.65 |
| Men's email | 21,307 | 18.28% | 1.25% | $1.42 |
| Women's email | 21,387 | 15.14% | 0.88% | $1.08 |

Preliminary mean differences versus control:

| Contrast | Incremental revenue/customer | 95% CI | Conversion lift |
|---|---:|---:|---:|
| Men's email - no email | $0.77 | $0.49 to $1.05 | +0.68 percentage points |
| Women's email - no email | $0.42 | $0.17 to $0.68 | +0.31 percentage points |

Because spend is zero-inflated and right-skewed, the final revenue analysis will pair the mean difference—the business estimand—with bootstrap and randomization-based uncertainty checks. Purchaser-only spend is descriptive, not the primary causal result, because conditioning on conversion occurs after treatment.

## Analysis contract

- **Experimental unit:** customer
- **Assignment:** three-arm randomized experiment
- **Primary estimand:** intent-to-treat difference in mean two-week spend per assigned customer
- **Primary contrasts:** men's email vs control; women's email vs control
- **Secondary outcomes:** conversion and visit rates
- **Exploratory contrast:** men's email vs women's email
- **Multiplicity:** Holm adjustment within each outcome family
- **Decision scope:** incremental gross revenue, not profit
- **Segment analysis:** exploratory and clearly separated from confirmatory results

See [docs/analysis_plan.md](docs/analysis_plan.md) for the full statistical plan and [docs/data_dictionary.md](docs/data_dictionary.md) for field definitions.

## Repository structure

```text
retail-email-abn-testing/
├── README.md
├── data/
│   └── README.md
├── docs/
│   ├── analysis_plan.md
│   └── data_dictionary.md
├── notebooks/
│   └── README.md
├── reports/
│   └── initial_dataset_audit.md
├── src/
│   ├── analyze_experiment.py
│   └── validate_data.py
├── .gitignore
└── requirements.txt
```

## Reproduce the audit

1. Download the CSV from the original MineThatData challenge page.
2. Save it under `data/raw/`.
3. Create a virtual environment and install the requirements.
4. Run:

```bash
python src/validate_data.py --data data/raw/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv
python src/analyze_experiment.py --data data/raw/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv
```

## Planned releases

- **v0.1 — Audit and design:** schema validation, assignment checks, data dictionary, analysis contract
- **v0.2 — Confirmatory A/B/n analysis:** effect estimates, intervals, multiplicity, publication-quality figures
- **v0.3 — Experiment planning:** minimum detectable effects and next-test sample-size scenarios
- **v0.4 — Segment exploration:** heterogeneous effects with uncertainty and false-discovery safeguards
- **v1.0 — Decision package:** executive summary, reproducible notebook, SQL KPI layer, and final recommendation

## Data source and redistribution note

Source: Kevin Hillstrom, *MineThatData E-Mail Analytics and Data Mining Challenge* (March 20, 2008).

Challenge page: https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html

The author publicly released the file for analysis, but the original CSV does not appear to include a formal license. This starter project therefore does not redistribute the raw data. The repository should retain source attribution and use a download-or-place-locally workflow unless redistribution rights are confirmed.
