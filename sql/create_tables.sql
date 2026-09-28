CREATE TABLE IF NOT EXISTS studies
(
    nct_id TEXT PRIMARY KEY,
    brief_title TEXT,
    overall_status TEXT,
    study_type TEXT,
    enrollment_count INT,
    enrollment_type TEXT,
    primary_completion_date TEXT,
    primary_completion_date_type TEXT,
    start_date TEXT,
    completion_date TEXT,
    completion_date_type TEXT
);

CREATE TABLE IF NOT EXISTS review_queue
(
    nct_id TEXT,
    rule_id TEXT,
    field TEXT,
    observed_value TEXT,
    reason TEXT,
    review_status TEXT,
    PRIMARY KEY (nct_id, rule_id),
    FOREIGN KEY (nct_id) REFERENCES studies(nct_id)
);