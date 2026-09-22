import json
from pathlib import Path
from quality_rules import needs_completion_date_review, build_completion_date_review_queue

# Locate the file relative to this script.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "lung_cancer_studies.json"

# Load the JSON into Python dictionaries and lists.
with DATA_PATH.open("r", encoding="utf-8") as file:
    data = json.load(file)

ids_to_inspect = {
    "NCT00119470",  # Enrollment count present, type missing.
    "NCT00103831",  # Completed, with several missing fields.
}

for study in data["studies"]:
    protocol = study["protocolSection"]
    nct_id = protocol["identificationModule"]["nctId"]

    if nct_id in ids_to_inspect:
        print(f"\nStudy: {nct_id}")

        for module_name in ["statusModule", "designModule"]:
            print(f"\n{module_name}:")
            print(json.dumps(
                protocol.get(module_name),
                indent=2,
                ensure_ascii=False,
            ))

def extract_study_summary(study):
    protocol = study["protocolSection"]
    identification = protocol["identificationModule"]
    status = protocol["statusModule"]
    design = protocol["designModule"]

    enrollment = design.get("enrollmentInfo", {})

    enrollment_count = enrollment.get("count")
    enrollment_type = enrollment.get("type")

    start = status.get("startDateStruct", {})

    start_date = start.get("date")

    primary_completion = status.get("primaryCompletionDateStruct", {})

    primary_completion_date = primary_completion.get("date")
    primary_completion_date_type = primary_completion.get("type")

    completion = status.get("completionDateStruct", {})

    completion_date = completion.get("date")
    completion_date_type = completion.get("type")

    study_summary = {
        "nct_id": identification["nctId"],
        "brief_title": identification["briefTitle"],
        "overall_status": status["overallStatus"],
        "study_type": design["studyType"],
        "enrollment_count": enrollment_count,
        "enrollment_type": enrollment_type,
        "primary_completion_date": primary_completion_date,
        "primary_completion_date_type": primary_completion_date_type,
        "start_date": start_date,
        "completion_date": completion_date,
        "completion_date_type": completion_date_type
    }

    return study_summary

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

review_queue = build_completion_date_review_queue(summaries)

OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "completion_date_review_queue.json"

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT_PATH.open("w", encoding="utf-8") as file:
    json.dump(review_queue, file, indent=2, ensure_ascii=False)
