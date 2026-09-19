# Clinical Trial Data Quality Monitor

## Business Problem

Incomplete or inconsistent clinical trial metadata can reduce the reliability of life sciences analysis. Data teams need a systematic way to identify potential issues, assess their impact and prioritize records for review.

## Objective

Build a reproducible workflow that detects potential data quality issues in public clinical trial metadata, explains each flag and helps reviewers prioritize investigations.

Flags indicate records requiring review, rather than confirmed errors.

## Initial Scope

The first version will analyze 100 study records returned by a lung cancer search on ClinicalTrials.gov.

The project uses publicly available study metadata, not patient-level data. Initial checks will focus on missing fields, duplicate study identifiers and inconsistent dates, accounting for differences in study design.

## Expected Outputs

- **Python/SQL pipeline:** extract, transform and validate study metadata.
- **Documented quality checks:** define each rule, its rationale and when it applies.
- **Prioritized review queue:** identify flagged records and explain why they need investigation.
- **Power BI dashboard:** summarize data quality findings and support record-level review.

## Author

**Ignacio Spreafico**
Data Analytics & Applied Data Science | Machine Learning & Automation | Python & SQL

📧 Email: nachospreafico06@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/ignacio-spreafico
📊 Portfolio: https://ignaciospreafico.vercel.app
🐙 GitHub: https://github.com/nachospreafico
