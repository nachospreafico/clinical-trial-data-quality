SELECT
    rule_id,
    COUNT(*) AS finding_count
FROM review_queue
GROUP BY rule_id;