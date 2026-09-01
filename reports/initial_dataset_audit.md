# Initial Dataset Audit

## Audit conclusion

The dataset is suitable for a portfolio-grade A/B/n experiment analysis. Assignment counts are consistent with equal randomization, pretreatment covariates are well balanced, and outcome logic is internally coherent.

## Structure and quality

- 64,000 rows and 12 fields
- 0 missing cells
- 0 invalid values across binary fields
- 0 negative prior-history or outcome-spend values
- 0 conversions without a visit
- 0 positive-spend records without conversion
- 0 conversions with zero spend
- 6,562 identical observed rows; retained because no customer ID exists

## Assignment validation

| Arm | Count | Share |
|---|---:|---:|
| Men's email | 21,307 | 33.29% |
| No email | 21,306 | 33.29% |
| Women's email | 21,387 | 33.42% |

Sample-ratio mismatch test against equal thirds: chi-square = 0.2025, p = 0.9037. There is no evidence of an assignment-count anomaly.

The largest observed standardized difference across `recency`, `history`, `mens`, `womens`, and `newbie` is below 0.009. Cramer's V is at most 0.010 across historical-spend band, geography, and channel. These are negligible imbalances.

## Preliminary outcomes

| Arm | Visit | Conversion | Revenue/customer | Total revenue |
|---|---:|---:|---:|---:|
| No email | 10.62% | 0.57% | $0.65 | $13,908.33 |
| Men's email | 18.28% | 1.25% | $1.42 | $30,311.69 |
| Women's email | 15.14% | 0.88% | $1.08 | $23,038.11 |

Welch mean-difference checks produce:

- Men's email vs control: +$0.7698 per customer; 95% CI $0.4851 to $1.0545
- Women's email vs control: +$0.4244 per customer; 95% CI $0.1690 to $0.6799
- Men's email vs women's email: +$0.3454 per customer; 95% CI $0.0326 to $0.6583

These are preliminary checks. The direct treatment comparison is exploratory, and final revenue inference should be verified with bootstrap and randomization-based methods because spend is sparse and right-skewed.

## Material limitations

- No email-delivery cost, product margin, discounts, returns, or unsubscribe outcome
- No customer identifier
- No observation timestamps within the two-week window
- No documented blocking or stratification variables
- No formal raw-data license included with the source file

The project can estimate incremental gross revenue and behavioral response, but it cannot establish incremental profit or long-term customer value.

