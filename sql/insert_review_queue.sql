INSERT INTO review_queue (
    nct_id,
    rule_id,
    field,
    observed_value,
    reason,
    review_status
)
VALUES (
    ?,
    ?,
    ?,
    ?,
    ?,
    ?
);