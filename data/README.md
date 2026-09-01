# Data

The raw Hillstrom CSV is intentionally excluded from version control because the original public challenge does not include clear formal redistribution terms.

Download the file from the source linked on the original challenge page and place it in:

```text
data/raw/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv
```

Original challenge page:

https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html

Expected source-file audit:

- 64,000 rows
- 12 columns
- no missing values
- three experiment arms
- source label `Surburban` retained in raw data
- SHA-256: `0e5893329d8b93cefecc571777672028290ab69865718020c78c7284f291aece`

Generated processed data belongs in `data/processed/` and must be reproducible from code.
