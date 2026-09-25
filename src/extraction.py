def extract_study_summary(study):
    protocol = study["protocolSection"]
    identification = protocol["identificationModule"]
    status = protocol["statusModule"]
    design = protocol["designModule"]

    enrollment = design.get("enrollmentInfo", {})
    if enrollment is None:
        enrollment = {}

    enrollment_count = enrollment.get("count")
    enrollment_type = enrollment.get("type")

    start = status.get("startDateStruct", {})

    if start is None:
        start = {}

    start_date = start.get("date")

    primary_completion = status.get("primaryCompletionDateStruct", {})

    if primary_completion is None:
        primary_completion = {}

    primary_completion_date = primary_completion.get("date")
    primary_completion_date_type = primary_completion.get("type")

    completion = status.get("completionDateStruct", {})

    if completion is None:
        completion = {}

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