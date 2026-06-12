from agent.recommendation_agent import generate_recommendation

result = {
    "match_score": 66.4,
    "matched_skills": [
        "deep learning",
        "pytorch",
        "computer vision"
    ],
    "missing_skills": [
        "medical image analysis",
        "python"
    ]
}

print(
    generate_recommendation(result)
)