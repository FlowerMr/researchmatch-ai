from agent.llm import llm


def generate_recommendation(result):

    prompt = f"""
    You are a PhD application advisor.

    Match score:
    {result["match_score"]}

    Matched skills:
    {result["matched_skills"]}

    Missing skills:
    {result["missing_skills"]}

    Give practical recommendations
    to improve the application.

    Keep it concise.
    """

    response = llm.invoke(prompt)

    return response.content