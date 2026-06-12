def analyze_gap(cv_data, position_data):

    cv_skills = [
        s.lower()
        for s in cv_data.get("skills", [])
    ]

    required_skills = [
        s.lower()
        for s in position_data.get(
            "required_skills",
            []
        )
    ]

    matched = []
    missing = []

    for skill in required_skills:

        if skill in cv_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    total = len(required_skills)

    if total == 0:
        score = 0
    else:
        score = round(
            len(matched) / total * 100,
            2
        )

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }