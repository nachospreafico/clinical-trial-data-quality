# Clinical Trial Data Quality Monitor

## Business Problem

Incomplete or inconsistent clinical trial metadata can reduce the reliability of life sciences analysis. Data teams need a systematic way to identify potential issues, assess their impact and prioritize records for review.

## Objective

Build a reproducible workflow that detects potential data quality issues in public clinical trial metadata, explains each flag and helps reviewers prioritize investigations.

Flags indicate records requiring review rather than confirmed errors.

## Scope

The current implementation analyzes 100 study records returned by a lung cancer search on ClinicalTrials.gov.

The project uses publicly available study metadata rather than patient-level data. Data quality checks cover missing fields, duplicate study identifiers and date consistency, with rule applicability determined by study characteristics where appropriate.

## Architecture

The project follows a simple data quality workflow:

**ClinicalTrials.gov → Python → DuckDB → Data Quality Rules → Review Queue → SQL Quality Reporting**

1. Clinical trial metadata is extracted from ClinicalTrials.gov.
2. Python transforms the raw API response into a structured study dataset.
3. Structured data and quality findings are persisted in DuckDB.
4. Documented data quality rules identify records requiring investigation.
5. Flagged records are consolidated into a review queue.
6. SQL queries provide record-level detail and aggregate quality metrics.

## Project Outputs

- **Reproducible Python pipeline:** extracts, transforms and validates clinical trial metadata.
- **DuckDB analytical layer:** stores structured study data and data quality findings for SQL analysis.
- **Documented data quality rules:** each rule defines its scope, rationale and review criteria.
- **Prioritized review queue:** surfaces study-level findings requiring investigation without treating flags as confirmed errors.
- **SQL quality reporting:** summarizes findings by rule and provides an overall view of dataset quality.
- **Automated tests:** validate data quality logic and review-queue generation.
- **Exportable outputs:** generates analysis-ready results for downstream review or reporting.

## Data Quality Approach

The project treats data quality findings as **review signals rather than confirmed errors**.

Rules are designed to account for study characteristics where relevant. A missing or unusual value is therefore only flagged when the corresponding rule determines that the record warrants investigation.

This approach reduces false positives and produces a review queue that can be used as an operational data quality workflow rather than simply reporting missing values.

## Technology

- **Python** — data extraction, transformation and validation
- **DuckDB** — analytical storage and querying
- **SQL** — quality metrics and record-level analysis
- **pytest** — automated testing
- **JSON / CSV** — raw and processed data outputs
- **Git / GitHub** — version control and project documentation

## Author

**Ignacio Spreafico**  
Data Analytics & Applied Data Science | Machine Learning & Automation | Python & SQL

📧 Email: nachospreafico06@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/ignacio-spreafico  
📊 Portfolio: https://ignaciospreafico.vercel.app  
🐙 GitHub: https://github.com/nachospreafico
