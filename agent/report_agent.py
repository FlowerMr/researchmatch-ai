def generate_report(
        cv_data,
        position_data,
        professor_data,
        match_score,
        professor_match,
        recommendation,
        critique
):

    return {
        "cv": cv_data,
        "position": position_data,
        "professor": professor_data,
        "match_score": match_score,
        "professor_match": professor_match,
        "recommendation": recommendation,
        "critique": critique
    }
    