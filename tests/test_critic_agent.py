from agent.critic_agent import critique_application

sample = {
    "match_score": 64.8,
    "recommendation": """
    Improve medical imaging experience.
    Highlight XAI research.
    """
}

print(
    critique_application(sample)
)