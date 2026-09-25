import pytest
from src.extraction import extract_study_summary

@pytest.fixture
def sample_study():
    return {
        "protocolSection":{
            "identificationModule": {
                "nctId": "STU-TEST-001",
                "briefTitle": "Test brief title"
            },
            "statusModule": {
                "overallStatus": "COMPLETED",
                "startDateStruct": {
                    "date": "2026-01"
                },
                "primaryCompletionDateStruct": {
                    "date": "2026-03",
                    "type": "ACTUAL"
                },
                "completionDateStruct": {
                    "date": "2026-03-31",
                    "type": "ACTUAL"
                }
            },
            "designModule": {
                "studyType": "OBSERVATIONAL",
                "enrollmentInfo": {
                    "count": 40,
                    "type": "ACTUAL"
                }
            }
        }
    }

@pytest.fixture
def sample_expected_output():
    return {
        "nct_id": "STU-TEST-001",
        "brief_title": "Test brief title",
        "overall_status": "COMPLETED",
        "study_type": "OBSERVATIONAL",
        "enrollment_count": 40,
        "enrollment_type": "ACTUAL",
        "primary_completion_date": "2026-03",
        "primary_completion_date_type": "ACTUAL",
        "start_date": "2026-01",
        "completion_date": "2026-03-31",
        "completion_date_type": "ACTUAL"
    }

def test_function_correctly_outputs_when_given_a_valid_study(sample_study, sample_expected_output):
    func_output = extract_study_summary(sample_study)
    assert func_output == sample_expected_output

@pytest.mark.parametrize(
    "removed_obj, expected_none",
    [
        ("designModule.enrollmentInfo", ["enrollment_count", "enrollment_type"]),
        ("statusModule.startDateStruct", ["start_date"]),
        ("statusModule.primaryCompletionDateStruct", ["primary_completion_date", "primary_completion_date_type"]),
        ("statusModule.completionDateStruct", ["completion_date", "completion_date_type"])
    ]
)
def test_extract_study_summary_handles_missing_optional_objects(sample_study, sample_expected_output, removed_obj, expected_none):
    module_name, object_name = removed_obj.split(".")
    del sample_study["protocolSection"][module_name][object_name]
    for key in expected_none:
        sample_expected_output[key] = None
    func_output = extract_study_summary(sample_study)
    assert func_output == sample_expected_output

@pytest.mark.parametrize(
    "module, none_obj",
    [
        ("designModule.enrollmentInfo", ["enrollment_count", "enrollment_type"]),
        ("statusModule.startDateStruct", ["start_date"]),
        ("statusModule.primaryCompletionDateStruct", ["primary_completion_date", "primary_completion_date_type"]),
        ("statusModule.completionDateStruct", ["completion_date", "completion_date_type"])
    ]
)
def test_extract_study_summary_handles_none_optional_objects(sample_study, sample_expected_output, module, none_obj):
    module_name, object_name = module.split(".")
    sample_study["protocolSection"][module_name][object_name] = None
    for key in none_obj:
        sample_expected_output[key] = None
    func_output = extract_study_summary(sample_study)
    assert func_output == sample_expected_output