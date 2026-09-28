from pathlib import Path
import duckdb
import json

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / "data" / "clinical_trials.duckdb"

DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

SCHEMA_PATH = PROJECT_ROOT / "sql" / "create_tables.sql"
schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")

SUMMARIES_PATH = PROJECT_ROOT / "data" / "processed" / "study_summaries.json"
REVIEW_PATH = PROJECT_ROOT / "data" / "processed" / "review_queue.json"

with SUMMARIES_PATH.open("r", encoding="utf-8") as file:
    summaries = json.load(file)

with REVIEW_PATH.open("r", encoding="utf-8") as file:
    review_queue = json.load(file)

print(f"Studies loaded: {len(summaries)}")
print(f"Findings loaded: {len(review_queue)}")

study_rows = [
    (
        study["nct_id"],
        study["brief_title"],
        study["overall_status"],
        study["study_type"],
        study["enrollment_count"],
        study["enrollment_type"],
        study["primary_completion_date"],
        study["primary_completion_date_type"],
        study["start_date"],
        study["completion_date"],
        study["completion_date_type"],
    )
    for study in summaries
]

review_rows = [
    (
        review["nct_id"],
        review["rule_id"],
        review["field"],
        review["observed_value"],
        review["reason"],
        review["review_status"]
    )
    for review in review_queue
]

INSERT_STUDIES_PATH = PROJECT_ROOT / "sql" / "insert_studies.sql"
insert_studies_sql = INSERT_STUDIES_PATH.read_text(encoding="utf-8")

INSERT_REVIEWS_PATH = PROJECT_ROOT / "sql" / "insert_review_queue.sql"
insert_review_queues_sql = INSERT_REVIEWS_PATH.read_text(encoding="utf-8")

with duckdb.connect(str(DATABASE_PATH)) as connection:
    connection.execute("BEGIN TRANSACTION")

    try:
        # Remove the dependent table first.
        connection.execute("DROP TABLE IF EXISTS review_queue")
        connection.execute("DROP TABLE IF EXISTS studies")

        # Recreate both tables and their constraints.
        connection.execute(schema_sql)

        # Insert parent records before their findings.
        if study_rows:
            connection.executemany(insert_studies_sql, study_rows)

        if review_rows:
            connection.executemany(insert_review_queues_sql, review_rows)

        connection.execute("COMMIT")

    except Exception:
        connection.execute("ROLLBACK")
        raise

    connection.sql(
        "SELECT COUNT(*) AS studies_loaded FROM studies"
    ).show()

    connection.sql(
        "SELECT COUNT(*) AS findings_loaded FROM review_queue"
    ).show()