from src.extraction import extract_study_summary

def test_function_correctly_outputs_when_given_a_valid_study():
    sample_study = {
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
    expected_output = {
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
    func_output = extract_study_summary(sample_study)
    assert func_output == expected_output