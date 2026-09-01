# Statistical Analysis Plan

## 1. Decision and causal question

Estimate whether either promotional email changes two-week customer behavior relative to sending no email and determine which campaign produces the larger incremental gross-revenue response.

The randomized assignment supports causal intent-to-treat estimates at the campaign-arm level. It does not identify profit because the dataset omits email delivery cost, product margin, discounts, and returns.

## 2. Units, arms, and analysis population

- Unit of randomization and analysis: customer record
- Arms: `No E-Mail`, `Mens E-Mail`, `Womens E-Mail`
- Population: all 64,000 randomized records
- Analysis principle: intent to treat; analyze every record in its assigned arm
- Exclusions: none unless a reproducible data-integrity rule is documented before outcome analysis

## 3. Outcomes and estimands

### Primary outcome

`spend`: two-week gross revenue per assigned customer.

For each treatment, estimate:

`mean(spend | treatment) - mean(spend | control)`

The absolute dollar difference is the primary effect. Relative lift is secondary because the control mean is small and can make percentages appear dramatic.

### Secondary outcomes

- `conversion`: absolute difference in conversion probability
- `visit`: absolute difference in visit probability

For binary outcomes, report counts, rates, risk differences, relative lifts, and 95% confidence intervals.

### Contrasts

Confirmatory:

1. Men's email vs no email
2. Women's email vs no email

Exploratory:

3. Men's email vs women's email

## 4. Experiment validation

Run before interpreting outcomes:

1. Schema, type, and allowed-value validation
2. Missingness and impossible-outcome checks
3. Sample-ratio mismatch chi-square test against equal thirds
4. Pretreatment covariate balance by standardized mean differences
5. Categorical balance by chi-square and Cramer's V
6. Distribution and outlier review for `history` and `spend`

Do not remove repeated rows solely because every observed field repeats. No customer identifier exists, so identical observations are not evidence that the same experimental unit was duplicated.

## 5. Inference

### Revenue per customer

- Point estimate: difference in arithmetic means
- Main interval: nonparametric bootstrap confidence interval for the mean difference
- Design-based check: permutation/randomization inference under no treatment effect
- Sensitivity check: Welch confidence interval and heteroskedasticity-robust regression

The arithmetic mean is retained because total incremental revenue equals customers exposed multiplied by incremental mean revenue. A rank test answers a different question and is not a substitute for inference on the mean.

### Conversion and visit

- Point estimate: risk difference
- Interval: score/Newcombe-style confidence interval
- Test: two-sample proportion test

### Multiple comparisons

Apply Holm correction within each outcome family across the two treatment-versus-control contrasts. Report both raw and adjusted p-values. Treat the direct treatment-versus-treatment contrast and all segments as exploratory.

Statistical significance is not sufficient for a recommendation. Report effect magnitude, interval width, operational relevance, and constraints.

## 6. Power and sensitivity

Use the observed control rates only as planning inputs for a future experiment—not as post-hoc proof that this experiment was adequately powered.

Initial sensitivity estimates at 80% power and two-sided alpha 0.025:

- Control conversion rate: 0.573%
- Per-arm sample size: approximately 21,300
- Detectable conversion rate: approximately 0.821%
- Minimum detectable absolute change: approximately 0.249 percentage points
- Approximate revenue sensitivity: $0.45 per customer, subject to skew and variance assumptions

The final project will provide sample-size curves across commercially meaningful effect sizes.

## 7. Segment analysis

Candidate pretreatment dimensions:

- new vs existing customer
- prior men's or women's merchandise purchase
- recency band
- historical spend band
- prior purchase channel
- geography category

Segment findings will be labeled exploratory. Report treatment-by-segment interaction estimates rather than declaring differences because one subgroup is significant and another is not. Use minimum cell-size rules, uncertainty intervals, and false-discovery control. A later release may compare predeclared segmentation with causal forests or uplift models using honest train/test splits.

## 8. Decision rules

A campaign can be described as increasing an outcome when its adjusted interval excludes zero and the effect is operationally meaningful. The final recommendation must distinguish:

- evidence that sending an email causes incremental revenue,
- evidence that one creative outperforms the other,
- evidence that targeting improves expected incremental value, and
- unanswered profit questions caused by missing cost and margin data.

## 9. Reproducibility

- Preserve the source file unchanged outside version control.
- Normalize known labels only in a processed copy; for example, map `Surburban` to `Suburban` while retaining the original value in the raw layer.
- Set random seeds for bootstrap, permutation, and modeling work.
- Export analysis-ready tables and figures from code.
- Record package versions in the final release.

