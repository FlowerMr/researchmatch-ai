from agent.llm import llm
import json
import re


def clean_json_response(content):

    content = content.strip()

    if content.startswith("```json"):
        content = content[7:]

    elif content.startswith("```"):
        content = content[3:]

    if content.endswith("```"):
        content = content[:-3]

    match = re.search(r"\{.*\}", content, re.DOTALL)

    if match:
        content = match.group()

    return content.strip()


def analyze_position(job_text):

    prompt = f"""
    Analyze this PhD position.

    Extract:

    1. Required Skills
    2. Research Topics
    3. Preferred Qualifications
    4. Keywords

    Return ONLY valid JSON:

    {{
      "required_skills": [],
      "research_topics": [],
      "preferred_qualifications": [],
      "keywords": []
    }}

    Position:

    {job_text}
    """

    response = llm.invoke(prompt)

    cleaned = clean_json_response(response.content)

    return json.loads(cleaned)