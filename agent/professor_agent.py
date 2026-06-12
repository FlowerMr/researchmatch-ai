import json
import re

from agent.llm import llm


def clean_json_response(content):

    content = content.strip()

    if content.startswith("```json"):
        content = content[7:]

    if content.endswith("```"):
        content = content[:-3]

    match = re.search(
        r"\{.*\}",
        content,
        re.DOTALL
    )

    if match:
        content = match.group()

    return content


def analyze_professor(text):

    prompt = f"""
    Analyze this professor profile.

    Extract:

    1. Research Interests
    2. Recent Topics
    3. Keywords

    Return ONLY JSON.

    Profile:

    {text}
    """

    response = llm.invoke(prompt)

    return json.loads(
        clean_json_response(
            response.content
        )
    )