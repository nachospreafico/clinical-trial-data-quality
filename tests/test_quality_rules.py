import pytest

"""
Study type	Status	Completion date	Expected
INTERVENTIONAL	COMPLETED	None	True
OBSERVATIONAL	COMPLETED	None	True
INTERVENTIONAL	COMPLETED	"2020-06"	False
INTERVENTIONAL	RECRUITING	None	False
INTERVENTIONAL	UNKNOWN	None	False
EXPANDED_ACCESS	COMPLETED	None	False
"""

@pytest.mark.parametrize(
    "study_type, status, completion_date, expected",
    [

    ]
)
def test_function_correctly_classifies_need_of_completion_date_review(study_type, status, completion_date, expected):
    pass