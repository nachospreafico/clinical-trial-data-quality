## Rule DQ001: Missing Completion Date

- **Purpose:** Identify completed studies with no reported completion date.
- **Applies to:** `INTERVENTIONAL` and `OBSERVATIONAL` studies.
- **Trigger:** `overall_status` is `COMPLETED` and extracted `completion_date` is `None`.
- **Interpretation:** Requires review; does not establish a source error or regulatory violation.
- **Handling:** Preserve the source values. Do not substitute the primary completion date.
- **Initial result:** Four findings in the initial saved dataset of 100 records.
