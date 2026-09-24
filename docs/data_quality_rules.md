## Rule DQ001: Missing Completion Date

- **Purpose:** Identify completed studies with no reported completion date.
- **Applies to:** `INTERVENTIONAL` and `OBSERVATIONAL` studies.
- **Trigger:** `overall_status` is `COMPLETED` and extracted `completion_date` is `None`.
- **Interpretation:** Requires review; does not establish a source error or regulatory violation.
- **Handling:** Preserve the source values. Do not substitute the primary completion date.
- **Initial result:** Four findings in the initial saved dataset of 100 records.

## Rule DQ002: Missing Enrollment Type

- **Purpose:** identify a reported enrollment count without its type.
- **Applies to:** interventional and observational studies, regardless of status.
- **Trigger:** count is not None and type is None. Zero counts qualify.
- **Interpretation:** review needed; the count cannot be classified as actual or estimated.
- **Handling:** preserve the count and missing type; do not infer the type.
- **Initial result:** one finding, NCT00119470, in the saved 100-record dataset.
