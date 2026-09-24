import json
from pathlib import Path
from quality_rules import build_review_queue
from extraction import extract_study_summary

# Locate the file relative to this script.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "lung_cancer_studies.json"

# Load the JSON into Python dictionaries and lists.
with DATA_PATH.open("r", encoding="utf-8") as file:
    data = json.load(file)

summaries = []

for study in data["studies"]:
    summary = extract_study_summary(study)
    summaries.append(summary)

fields_to_review = [
    "enrollment_count",
    "enrollment_type",
    "start_date",
    "completion_date",
    "completion_date_type",
]

review_queue = build_review_queue(summaries)

OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "review_queue.json"

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT_PATH.open("w", encoding="utf-8") as file:
    json.dump(review_queue, file, indent=2, ensure_ascii=False)

print(f"Studies processed: {len(summaries)}")
print(f"Findings requiring review: {len(review_queue)}")
print(f"Review queue saved to: {OUTPUT_PATH}")