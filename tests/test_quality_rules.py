import pytest
from src.quality_rules import needs_completion_date_review, build_completion_date_review_queue

@pytest.mark.parametrize(
    "study_type, status, completion_date, expected",
    [
        ("INTERVENTIONAL", "COMPLETED", None, True),
        ("OBSERVATIONAL", "COMPLETED", None, True),
        ("INTERVENTIONAL", "COMPLETED", "2020-06", False),
        ("INTERVENTIONAL", "RECRUITING", None, False),
        ("INTERVENTIONAL", "UNKNOWN", None, False),
        ("EXPANDED_ACCESS", "COMPLETED", None, False)
    ]
)
def test_function_correctly_classifies_need_of_completion_date_review(study_type, status, completion_date, expected):
    test_dict = {
        "study_type": study_type,
        "overall_status": status,
        "completion_date": completion_date
    }
    func_output = needs_completion_date_review(test_dict)
    assert func_output == expected

def test_function_correctly_outputs_an_empty_list_when_given_an_empty_list():
    sample_input = []
    func_output = build_completion_date_review_queue(sample_input)
    assert func_output == []

def test_function_correctly_outputs_an_empty_list_when_all_non_qualifying_studies():
    sample_input = [
        {
            "nct_id": "TEST001",
            "study_type": "INTERVENTIONAL",
            "overall_status": "COMPLETED",
            "completion_date": "2020-06",
        },
        {
            "nct_id": "TEST002",
            "study_type": "OBSERVATIONAL",
            "overall_status": "RECRUITING",
            "completion_date": None,
        },
        {
            "nct_id": "TEST003",
            "study_type": "EXPANDED_ACCESS",
            "overall_status": "APPROVED_FOR_MARKETING",
            "completion_date": None,
        },
    ]
    func_output = build_completion_date_review_queue(sample_input)
    assert func_output == []

def test_function_correctly_outputs_when_given_a_mix_of_qualified_and_non_qualified_studies_are_passed():
    sample_input = [
        {
            "nct_id": "TEST001",
            "study_type": "INTERVENTIONAL",
            "overall_status": "COMPLETED",
            "completion_date": None,
        },
        {
            "nct_id": "TEST002",
            "study_type": "OBSERVATIONAL",
            "overall_status": "RECRUITING",
            "completion_date": None,
        },
        {
            "nct_id": "TEST003",
            "study_type": "OBSERVATIONAL",
            "overall_status": "COMPLETED",
            "completion_date": None,
        },
    ]
    expected_output = [
        {
            "nct_id": "TEST001",
            "rule_id": "DQ001",
            "field": "completion_date",
            "observed_value": None,
            "reason": "Completed study has no reported completion date.",
            "review_status": "PENDING"
        },
        {
            "nct_id": "TEST003",
            "rule_id": "DQ001",
            "field": "completion_date",
            "observed_value": None,
            "reason": "Completed study has no reported completion date.",
            "review_status": "PENDING"
        }
    ]
    func_output = build_completion_date_review_queue(sample_input)
    assert func_output == expected_output

def test_function_does_not_alter_original_input_list():
    sample_input = [
        {
            "nct_id": "TEST001",
            "study_type": "INTERVENTIONAL",
                "overall_status": "COMPLETED",
                "completion_date": None,
        },
        {
            "nct_id": "TEST002",
            "study_type": "OBSERVATIONAL",
            "overall_status": "RECRUITING",
            "completion_date": None,
        },
        {
            "nct_id": "TEST003",
            "study_type": "OBSERVATIONAL",
            "overall_status": "COMPLETED",
            "completion_date": None,
        },
    ]
    expected_input = [
        {
            "nct_id": "TEST001",
            "study_type": "INTERVENTIONAL",
                "overall_status": "COMPLETED",
                "completion_date": None,
        },
        {
            "nct_id": "TEST002",
            "study_type": "OBSERVATIONAL",
            "overall_status": "RECRUITING",
            "completion_date": None,
        },
        {
            "nct_id": "TEST003",
            "study_type": "OBSERVATIONAL",
            "overall_status": "COMPLETED",
            "completion_date": None,
        },
    ]
    build_completion_date_review_queue(sample_input)
    assert sample_input == expected_input