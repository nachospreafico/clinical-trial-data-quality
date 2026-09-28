SELECT
    rq.nct_id,
    s.brief_title,
    s.study_type,
    s.overall_status,
    rq.rule_id,
    rq.field,
    rq.observed_value,
    rq.reason,
    rq.review_status
FROM review_queue rq
LEFT JOIN studies s
ON rq.nct_id = s.nct_id;