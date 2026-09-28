from pathlib import Path
import duckdb

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / "data" / "clinical_trials.duckdb"
REVIEW_QUEUE_PATH = PROJECT_ROOT / "sql" / "review_queue_details.sql"
FINDINGS_BY_RULE_PATH = PROJECT_ROOT / "sql" / "findings_by_rule.sql"
QUALITY_OVERVIEW_PATH = PROJECT_ROOT / "sql" / "quality_overview.sql"

review_queue_details = REVIEW_QUEUE_PATH.read_text(encoding="utf-8")
findings_by_rule = FINDINGS_BY_RULE_PATH.read_text(encoding="utf-8")
quality_overview = QUALITY_OVERVIEW_PATH.read_text(encoding="utf-8")

print(repr(findings_by_rule))

with duckdb.connect(str(DATABASE_PATH), read_only=True) as connection:
    connection.sql(review_queue_details).show()
    connection.sql(findings_by_rule).show()
    connection.sql(quality_overview).show()