def needs_completion_date_review(summary):
    eligible_study_types = ["INTERVENTIONAL", "OBSERVATIONAL"]

    return (
        summary["study_type"] in eligible_study_types
        and summary["overall_status"] == "COMPLETED"
        and summary["completion_date"] is None
    )

def build_completion_date_review_queue(summaries):
    flagged_summaries = []
    for summary in summaries:
        if needs_completion_date_review(summary):
            curr_dict = {
                "nct_id": summary["nct_id"],
                "rule_id": "DQ001",
                "field": "completion_date",
                "observed_value": summary["completion_date"], # Should be None
                "reason": "Completed study has no reported completion date.",
                "review_status": "PENDING"
            }
            flagged_summaries.append(curr_dict)
    return flagged_summaries