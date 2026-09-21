import json
from pathlib import Path

# Locate the file relative to this script.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "lung_cancer_studies.json"

# Load the JSON into Python dictionaries and lists.
with DATA_PATH.open("r", encoding="utf-8") as file:
    data = json.load(file)

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
        "start_date": start_date,
        "completion_date": completion_date,
        "completion_date_type": completion_date_type
    }

    return study_summary

summaries = []

for study in data["studies"]:
    summary = extract_study_summary(study)
    summaries.append(summary)

for field in summaries[0]:
    missing_count = sum(
        summary[field] is None
        for summary in summaries
    )

    print(f"{field}: {missing_count} missing")