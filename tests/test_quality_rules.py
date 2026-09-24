import pytest
from src.quality_rules import needs_completion_date_review, build_review_queue, needs_enrollment_type_review

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
    func_output = build_review_queue(sample_input)
    assert func_output == []

def test_function_correctly_outputs_an_empty_list_when_all_non_qualifying_studies():
    sample_input = [
        {
            "nct_id": "TEST001",
            "study_type": "INTERVENTIONAL",
            "overall_status": "COMPLETED",
            "completion_date": "2020-06",
            "enrollment_count": 40,
            "enrollment_type": "ACTUAL"
        },
        {
            "nct_id": "TEST002",
            "study_type": "OBSERVATIONAL",
            "overall_status": "RECRUITING",
            "completion_date": None,
            "enrollment_count": 40,
            "enrollment_type": "ACTUAL"
        },
        {
            "nct_id": "TEST003",
            "study_type": "EXPANDED_ACCESS",
            "overall_status": "APPROVED_FOR_MARKETING",
            "completion_date": None,
            "enrollment_count": 40,
            "enrollment_type": "ACTUAL"
        },
    ]
    func_output = build_review_queue(sample_input)
    assert func_output == []

def test_function_correctly_outputs_when_given_a_mix_of_qualified_and_non_qualified_studies():
    sample_input = [
        {
            "nct_id": "TEST001",
            "study_type": "INTERVENTIONAL",
            "overall_status": "COMPLETED",
            "completion_date": None,
            "enrollment_count": 40,
            "enrollment_type": "ACTUAL"
        },
        {
            "nct_id": "TEST002",
            "study_type": "OBSERVATIONAL",
            "overall_status": "RECRUITING",
            "completion_date": None,
            "enrollment_count": 40,
            "enrollment_type": "ACTUAL"
        },
        {
            "nct_id": "TEST003",
            "study_type": "OBSERVATIONAL",
            "overall_status": "COMPLETED",
            "completion_date": None,
            "enrollment_count": 40,
            "enrollment_type": "ACTUAL"
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
    func_output = build_review_queue(sample_input)
    assert func_output == expected_output

def test_function_does_not_alter_original_input_list():
    sample_input = [
        {
            "nct_id": "TEST001",
            "study_type": "INTERVENTIONAL",
            "overall_status": "COMPLETED",
            "completion_date": None,
            "enrollment_count": 40,
            "enrollment_type": "ACTUAL",
        },
        {
            "nct_id": "TEST002",
            "study_type": "OBSERVATIONAL",
            "overall_status": "RECRUITING",
            "completion_date": None,
            "enrollment_count": 40,
            "enrollment_type": "ACTUAL",
        },
        {
            "nct_id": "TEST003",
            "study_type": "OBSERVATIONAL",
            "overall_status": "COMPLETED",
            "completion_date": None,
            "enrollment_count": 40,
            "enrollment_type": "ACTUAL",
        },
    ]
    expected_input = [
        {
            "nct_id": "TEST001",
            "study_type": "INTERVENTIONAL",
            "overall_status": "COMPLETED",
            "completion_date": None,
            "enrollment_count": 40,
            "enrollment_type": "ACTUAL",
        },
        {
            "nct_id": "TEST002",
            "study_type": "OBSERVATIONAL",
            "overall_status": "RECRUITING",
            "completion_date": None,
            "enrollment_count": 40,
            "enrollment_type": "ACTUAL",
        },
        {
            "nct_id": "TEST003",
            "study_type": "OBSERVATIONAL",
            "overall_status": "COMPLETED",
            "completion_date": None,
            "enrollment_count": 40,
            "enrollment_type": "ACTUAL",
        },
    ]
    build_review_queue(sample_input)
    assert sample_input == expected_input

@pytest.mark.parametrize(
        "study_type, enrollment_count, enrollment_type, expected",
        [
            ("INTERVENTIONAL", 40, None, True),
            ("OBSERVATIONAL",	40,	None,	True),
            ("INTERVENTIONAL",	0,	None,	True),
            ("INTERVENTIONAL",	40,	"ACTUAL",	False),
            ("INTERVENTIONAL",	40,	"ESTIMATED",	False),
            ("INTERVENTIONAL",	None,	None,	False),
            ("INTERVENTIONAL",	None,	"ACTUAL",	False),
            ("EXPANDED_ACCESS",	40,	None,	False),
        ]
)
def test_function_correctly_classifies_need_of_enrollment_type_review(study_type, enrollment_count, enrollment_type, expected):
    test_dict = {
        "study_type": study_type,
        "enrollment_count": enrollment_count,
        "enrollment_type": enrollment_type
    }
    func_output = needs_enrollment_type_review(test_dict)
    assert func_output == expected

def test_function_correctly_outputs_when_passed_a_DQ002_qualifying_summary():
    sample_input = [
        {
            "nct_id": "TEST001",
            "study_type": "INTERVENTIONAL",
            "overall_status": "COMPLETED",
            "completion_date": "2026-09-01",
            "enrollment_count": 40,
            "enrollment_type": None,
        }
    ]
    expected_output = [
        {
            "nct_id": "TEST001",
            "rule_id": "DQ002",
            "field": "enrollment_type",
            "observed_value": None,
            "reason": "Enrollment count is present but enrollment type is missing.",
            "review_status": "PENDING"
        }
    ]
    func_output = build_review_queue(sample_input)
    assert func_output == expected_output

def test_build_review_queue_returns_both_findings_for_one_study():
    sample_input = [
        {
            "nct_id": "TEST001",
            "study_type": "OBSERVATIONAL",
            "overall_status": "COMPLETED",
            "completion_date": None,
            "enrollment_count": 40,
            "enrollment_type": None
        }
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
            "nct_id": "TEST001",
            "rule_id": "DQ002",
            "field": "enrollment_type",
            "observed_value": None,
            "reason": "Enrollment count is present but enrollment type is missing.",
            "review_status": "PENDING"
        }
    ]
    func_output = build_review_queue(sample_input)
    assert func_output == expected_output