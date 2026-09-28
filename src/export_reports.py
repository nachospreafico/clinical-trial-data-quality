from pathlib import Path
import duckdb

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / "data" / "clinical_trials.duckdb"
REVIEW_QUEUE_PATH = PROJECT_ROOT / "sql" / "review_queue_details.sql"

review_queue_details = REVIEW_QUEUE_PATH.read_text(encoding="utf-8")

EXPORT_DIR = PROJECT_ROOT / "data" / "exports"
EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    
STUDIES_EXPORT_PATH = EXPORT_DIR / "studies.csv"
REVIEWS_EXPORT_PATH = EXPORT_DIR / "review_queue_details.csv"

with duckdb.connect(str(DATABASE_PATH), read_only=True) as connection:
    connection.sql("SELECT * FROM studies ORDER BY nct_id").write_csv(
        str(STUDIES_EXPORT_PATH),
        header=True,
    )

    connection.sql(review_queue_details).write_csv(
        str(REVIEWS_EXPORT_PATH),
        header=True,
    )

print(f"Studies exported to: {STUDIES_EXPORT_PATH}")
print(f"Findings exported to: {REVIEWS_EXPORT_PATH}")