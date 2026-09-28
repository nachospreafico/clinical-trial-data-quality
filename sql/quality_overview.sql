SELECT
    (SELECT COUNT(*) FROM studies) AS total_studies,
    (SELECT COUNT(*) FROM review_queue) AS total_findings,
    (SELECT COUNT(DISTINCT nct_id) FROM review_queue) AS studies_with_findings,
    (SELECT COUNT(DISTINCT nct_id) FROM review_queue) * 1.0 / NULLIF((SELECT COUNT(*) FROM studies), 0) * 100 AS studies_with_findings_pct;