def analyze_skill_gap(cv_data, position_data, match_score):

    cv_skills = set(
        skill.lower()
        for skill in cv_data.get("skills", [])
    )

    required_skills = set(
        skill.lower()
        for skill in position_data.get("required_skills", [])
    )

    matched_skills = list(
        cv_skills.intersection(required_skills)
    )

    missing_skills = list(
        required_skills - cv_skills
    )

    return {
        "match_score": match_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills
    }