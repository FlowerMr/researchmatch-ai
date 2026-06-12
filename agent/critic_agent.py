from agent.llm import llm


def critique_application(data):

    prompt = f"""
    You are a senior PhD reviewer.

    Analyze:

    Match Score:
    {data["match_score"]}

    Recommendation:
    {data["recommendation"]}

    Find:

    1. Weaknesses
    2. Missing skills
    3. Improvement suggestions

    Be concise.
    """

    response = llm.invoke(prompt)

    return response.content