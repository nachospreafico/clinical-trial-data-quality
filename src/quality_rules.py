def needs_completion_date_review(summary):
    eligible_study_types = ["INTERVENTIONAL", "OBSERVATIONAL"]

    return (
        summary["study_type"] in eligible_study_types
        and summary["overall_status"] == "COMPLETED"
        and summary["completion_date"] is None
    )