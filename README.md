# AI-Augmented Retail Email Experiment

### A/B/n testing, incremental revenue analysis, and customer targeting for a retail marketing decision

**Project status:** Phase 1 complete — dataset audit and experiment-analysis design  
**Current conclusion:** Both promotional emails produced better customer response than sending no email; the men's merchandise email produced the strongest preliminary overall results.

---

## Executive Summary

A retailer wanted to determine whether promotional email campaigns would increase customer visits, purchases, and revenue. A total of 64,000 customers were randomly divided into three groups:

- a control group that received no email;
- a group that received a men's merchandise email; and
- a group that received a women's merchandise email.

Customer behavior was measured for two weeks after the campaign. Preliminary results indicate that both emails improved customer response relative to sending no email. The men's email produced the highest visit rate, conversion rate, and revenue per customer.

The men's email generated approximately **$0.77 more gross revenue per customer** than the control group. The women's email generated approximately **$0.42 more gross revenue per customer** than the control group.

Expressed as a practical planning estimate, those results represent approximately:

- **$770 in additional gross revenue per 1,000 customers** for the men's email; and
- **$420 in additional gross revenue per 1,000 customers** for the women's email.

These are preliminary gross-revenue estimates, not profit estimates. The dataset does not include campaign costs, product margins, discounts, returns, or long-term customer behavior. Additional statistical validation will be completed before making a final campaign recommendation.

---

## Business Decision

This project is organized around one management question:

> **Should the retailer send a promotional email, which campaign should it use, and which customers should it target to maximize incremental revenue?**

The analysis is designed to provide decision-makers with four practical answers:

1. Can the experiment be trusted?
2. Did either email cause an increase in customer response?
3. Which email produced the larger incremental revenue effect?
4. Can future campaigns be targeted more effectively using customer history?

---

## What Was Tested

This is an **A/B/n experiment**, meaning that one control group was compared with more than one treatment group.

| Group | Customers | Campaign received |
|---|---:|---|
| Control | 21,306 | No email |
| Treatment 1 | 21,307 | Men's merchandise email |
| Treatment 2 | 21,387 | Women's merchandise email |

The experiment measured three customer outcomes during the two-week observation period:

- **Visit rate:** the percentage of customers who visited the retailer;
- **Conversion rate:** the percentage of customers who completed a purchase; and
- **Revenue per customer:** average gross revenue across every customer assigned to the group.

Revenue per customer is the primary business measure because it connects the experiment directly to the retailer's revenue decision. Visit and conversion rates help explain how the campaigns influenced customer behavior.

---

## Preliminary Findings

### Results by Experiment Group

| Experiment group | Customers | Visit rate | Conversion rate | Revenue per customer |
|---|---:|---:|---:|---:|
| No email | 21,306 | 10.62% | 0.57% | $0.65 |
| Men's email | 21,307 | 18.28% | 1.25% | $1.42 |
| Women's email | 21,387 | 15.14% | 0.88% | $1.08 |

### Estimated Improvement Over No Email

| Campaign comparison | Additional revenue per customer | 95% confidence interval | Conversion-rate increase |
|---|---:|---:|---:|
| Men's email compared with no email | $0.77 | $0.49 to $1.05 | +0.68 percentage points |
| Women's email compared with no email | $0.42 | $0.17 to $0.68 | +0.31 percentage points |

### Plain-Language Interpretation

- Both promotional emails produced higher visits, purchases, and revenue than sending no email.
- The men's email produced the strongest preliminary performance across all three outcomes.
- The estimated revenue improvement for each email is positive even after accounting for statistical uncertainty.
- A final decision should still consider campaign cost, profit margin, customer fatigue, and whether the results remain consistent across customer segments.

A 95% confidence interval describes the range of effects that is reasonably compatible with the experiment data and statistical method. It is more informative than reporting only whether a result is statistically significant.

---

## Can the Experiment Be Trusted?

Before comparing campaign performance, the project evaluated whether the dataset and random assignment were credible.

| Validation check | Result |
|---|---:|
| Customer records | 64,000 |
| Data fields | 12 |
| Missing values | 0 |
| Invalid binary values | 0 |
| Conversions without a recorded visit | 0 |
| Positive spend without conversion | 0 |
| Sample-ratio mismatch test | p = 0.904 |
| Largest standardized difference across numeric customer characteristics | 0.009 |

The three groups contain nearly equal numbers of customers, and their pre-campaign characteristics are closely balanced. There is no evidence of a meaningful assignment-count problem or data-integrity failure.

The file contains 6,562 rows with identical observed values. These rows are retained because the source does not provide customer identifiers. Two different customers can share the same recorded characteristics and outcomes, so identical rows are not sufficient evidence that customers were duplicated.

Detailed validation results are available in [`reports/initial_dataset_audit.md`](reports/initial_dataset_audit.md).

---

## How AI Supports This Project

The statistical calculations are performed with reproducible Python code. AI is not used to manufacture experiment results or replace statistical validation.

The planned AI-augmented layer will support the project by:

- translating verified statistical outputs into plain-language decision summaries;
- identifying questions that business stakeholders may ask about the experiment;
- comparing technical findings with the business decision and documented limitations;
- generating draft executive narratives from validated result tables; and
- helping make the analysis accessible to both technical and nontechnical audiences.

All AI-generated explanations will be reviewed against the underlying Python outputs. Numerical results, confidence intervals, and campaign comparisons will remain traceable to reproducible analytical code.

This approach demonstrates responsible AI augmentation: AI assists with interpretation and communication while validated analytical methods remain the source of truth.

---

## Current Project Status

### Completed

- Established the business question and experiment-analysis plan
- Inspected all 64,000 customer records
- Validated field types, missingness, and outcome logic
- Checked experiment-group sizes for assignment anomalies
- Evaluated pretreatment customer balance across groups
- Calculated preliminary visit, conversion, and revenue measures
- Documented the data dictionary, analytical methods, and limitations
- Created reusable Python validation and analysis scripts

### In Progress

- Building the experiment-audit notebook
- Producing publication-quality validation figures
- Creating reproducible result tables for GitHub display

### Planned

- Bootstrap and randomization-based revenue inference
- Multiple-comparison adjustment
- Power and minimum detectable effect analysis
- Customer-segment treatment-effect analysis
- AI-assisted executive-summary workflow
- Final campaign recommendation and decision brief

---

## Analytical Approach

The project follows a decision-focused experimentation workflow:

1. **Define the decision.** Identify the campaign question and the measures that matter to management.
2. **Validate the experiment.** Confirm that the data are internally consistent and the randomized groups are comparable.
3. **Measure campaign effects.** Estimate the difference between each email group and the no-email control group.
4. **Quantify uncertainty.** Report confidence intervals and statistical tests instead of relying only on observed averages.
5. **Control repeated testing risk.** Adjust for the fact that multiple campaigns and outcomes are being compared.
6. **Evaluate business importance.** Separate statistically detectable changes from commercially meaningful changes.
7. **Explore customer differences.** Investigate whether campaign effectiveness varies by customer history or purchasing behavior.
8. **Communicate the decision.** Translate verified results into a concise management recommendation.

---

## Technical Analysis Framework

This section provides methodological detail for technical reviewers.

- **Experimental unit:** customer record
- **Assignment:** randomized three-arm experiment
- **Analysis population:** all 64,000 assigned customer records
- **Primary outcome:** two-week gross revenue per assigned customer
- **Primary estimand:** intent-to-treat difference in mean spend
- **Primary comparisons:** men's email vs no email; women's email vs no email
- **Secondary outcomes:** conversion and visit rates
- **Exploratory comparison:** men's email vs women's email
- **Multiple comparisons:** Holm adjustment within each outcome family
- **Segment analysis:** exploratory treatment-by-segment interaction estimates

### Revenue Analysis

Revenue is sparse and right-skewed because most customers did not purchase during the observation period. The final revenue analysis will use:

- difference in arithmetic mean revenue per assigned customer;
- nonparametric bootstrap confidence intervals;
- permutation or randomization-based inference;
- Welch confidence intervals as a sensitivity check; and
- heteroskedasticity-robust regression as an additional validation method.

The arithmetic mean remains the primary business measure because total incremental revenue is determined by the number of customers contacted multiplied by incremental average revenue per customer.

### Conversion and Visit Analysis

Binary outcomes will be reported using:

- customer counts;
- group rates;
- absolute percentage-point differences;
- relative lift;
- confidence intervals; and
- two-sample proportion tests.

The complete methodology is documented in [`docs/analysis_plan.md`](docs/analysis_plan.md).

---

## Dataset

The project uses the **MineThatData E-Mail Analytics and Data Mining Challenge** dataset published by Kevin Hillstrom in 2008.

The dataset includes pretreatment customer characteristics and post-campaign outcomes.

### Customer Characteristics

- months since the most recent purchase;
- historical customer spending;
- historical spending category;
- prior men's or women's merchandise purchases;
- new-customer indicator;
- previous purchase channel; and
- geographic-area category.

### Experiment and Outcome Fields

- assigned campaign group;
- visit indicator;
- conversion indicator; and
- two-week customer spend.

The full field guide is available in [`docs/data_dictionary.md`](docs/data_dictionary.md).

---

## Repository Structure

```text
AI_augmented_retail-email-a_b-testing/
├── README.md
├── data/
│   ├── README.md
│   ├── raw/
│   │   └── .gitkeep
│   └── processed/
│       └── .gitkeep
├── docs/
│   ├── analysis_plan.md
│   └── data_dictionary.md
├── notebooks/
│   └── README.md
├── reports/
│   ├── initial_dataset_audit.md
│   ├── figures/
│   │   └── .gitkeep
│   └── tables/
│       └── .gitkeep
├── src/
│   ├── analyze_experiment.py
│   └── validate_data.py
├── .gitignore
├── LICENSE
└── requirements.txt
```

| Location | Purpose |
|---|---|
| `data/` | Instructions for obtaining the source data and storing local raw or processed files |
| `docs/` | Statistical analysis plan and field definitions |
| `notebooks/` | Step-by-step analysis, explanations, and visual results |
| `reports/` | Audit results, final tables, figures, and decision summaries |
| `src/` | Reusable Python validation and statistical functions |

---

## Reproducing the Initial Audit

### 1. Clone the Repository

```bash
git clone https://github.com/stnguinn/AI_augmented_retail-email-a_b-testing.git
cd AI_augmented_retail-email-a_b-testing
```

### 2. Create a Python Environment

```bash
python -m venv .venv
```

Windows activation:

```bash
.venv\Scripts\activate
```

macOS or Linux activation:

```bash
source .venv/bin/activate
```

### 3. Install the Required Packages

```bash
pip install -r requirements.txt
```

### 4. Add the Source CSV Locally

Place the Hillstrom CSV in:

```text
data/raw/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv
```

The raw file is excluded from version control.

### 5. Run the Validation and Preliminary Analysis

```bash
python src/validate_data.py --data data/raw/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv

python src/analyze_experiment.py --data data/raw/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv
```

---

## Development Roadmap

| Release | Focus | Planned deliverables |
|---|---|---|
| v0.1 | Audit and design | Schema validation, assignment checks, data dictionary, analysis plan |
| v0.2 | Confirmatory analysis | Campaign-effect estimates, uncertainty intervals, multiplicity adjustment, figures |
| v0.3 | Experiment planning | Power analysis, minimum detectable effects, future sample-size scenarios |
| v0.4 | Customer targeting | Segment interactions, uncertainty controls, targeting recommendations |
| v0.5 | AI augmentation | Plain-language summaries, stakeholder Q&A, result-grounding checks |
| v1.0 | Decision package | Executive brief, reproducible notebooks, final visualizations, recommendation |

---

## Limitations and Responsible Interpretation

This project can estimate incremental short-term gross revenue and customer response. It cannot directly establish:

- campaign profitability;
- product-level margin effects;
- the effect of discounts or returns;
- email unsubscribes or customer fatigue;
- long-term customer value;
- customer-level treatment effects with certainty; or
- whether results will remain identical in a future campaign.

The source file also lacks customer identifiers. Identical rows therefore cannot be confirmed as duplicate customers and are retained unless additional evidence supports their removal.

Customer-segment findings will be treated as exploratory until they are supported by interaction tests, uncertainty intervals, appropriate validation, and false-discovery safeguards.

---

## Skills Demonstrated

This portfolio project demonstrates:

- business-question development;
- experimental design and A/B/n testing;
- data-quality and randomization validation;
- statistical inference and uncertainty communication;
- Python data analysis;
- revenue and conversion analysis;
- power and minimum detectable effect planning;
- causal and incremental-impact reasoning;
- responsible AI-assisted analytics; and
- communication for technical and nontechnical stakeholders.

---

## Data Source and Redistribution

**Source:** Kevin Hillstrom, *MineThatData E-Mail Analytics and Data Mining Challenge*, March 20, 2008.

Original challenge page:  
https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html

The author publicly released the file for analysis, but the original CSV does not appear to include a formal data license. This repository therefore does not redistribute the raw dataset. Users should obtain the file from the original source and store it locally under `data/raw/`.

---

## License

Repository code is currently distributed under the terms specified in the included [`LICENSE`](LICENSE) file. The source dataset is governed separately by its original publisher and is not included in this repository.

---

## Author

**Stanley Guinn, M.S.**  
Data and Decision Analytics | Enterprise Data Management | Statistical Analysis | AI-Augmented Analytics

GitHub: https://github.com/stnguinn
