# Data Dictionary

| Field | Type | Timing | Description | Validation |
|---|---|---|---|---|
| `recency` | integer | Pretreatment | Months since most recent purchase | 1–12 |
| `history_segment` | category | Pretreatment | Prior-year spend band | 7 ordered bands |
| `history` | numeric | Pretreatment | Prior-year customer spend | Nonnegative |
| `mens` | binary | Pretreatment | Purchased men's merchandise previously | 0 or 1 |
| `womens` | binary | Pretreatment | Purchased women's merchandise previously | 0 or 1 |
| `zip_code` | category | Pretreatment | Geography class | Urban, Surburban, Rural |
| `newbie` | binary | Pretreatment | New-customer indicator | 0 or 1 |
| `channel` | category | Pretreatment | Prior purchasing channel | Phone, Web, Multichannel |
| `segment` | category | Treatment | Randomized experiment arm | No E-Mail, Mens E-Mail, Womens E-Mail |
| `visit` | binary | Post-treatment | Visited during two-week outcome window | 0 or 1 |
| `conversion` | binary | Post-treatment | Converted during outcome window | 0 or 1; conversion implies visit |
| `spend` | numeric | Post-treatment | Spend during outcome window | Nonnegative; positive only for converters |

## Raw-data notes

- `Surburban` is the label found in the source file. A processed layer may rename it to `Suburban`, but the raw layer should remain unchanged.
- The file has no customer identifier. Do not interpret identical rows as confirmed duplicate customers.
- `history_segment` can be checked against `history`, but the numeric field should be used for modeling to avoid loss of information.
- `spend` is zero-inflated because non-converters have zero spend.

