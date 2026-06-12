import fitz; from agent.llm import llm; import json; import re
def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""
def clean_json_response(content):
    content = content.strip()
    if content.startswith("```json"):
        content = content[7:]
    elif content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]
    json_match = re.search(r'\{.*\}', content, re.DOTALL)
    if json_match:
        content = json_match.group()
    return content.strip()
def analyze_cv(pdf_path):
    try:
        cv_text = extract_text_from_pdf(pdf_path)
        if not cv_text:
            return {"error": "Could not extract text from PDF"}
        prompt = f"""
        Analyze this CV.
        Extract:
        1. Skills
        2. Education  
        3. Projects
        4. Research Interests
        Return ONLY valid JSON format like this (no markdown, no backticks, no extra text):
        {{
            "skills": ["skill1", "skill2"],
            "education": ["degree1", "degree2"],
            "projects": ["project1", "project2"],
            "research_interests": ["interest1", "interest2"]
        }}
        CV:
        {cv_text[:3000]}
        """
        response = llm.invoke(prompt)
        cleaned_content = clean_json_response(response.content)
        result = json.loads(cleaned_content)
        return result
    except json.JSONDecodeError as e:
        return {"error": f"Invalid JSON response: {str(e)}", "raw_response": response.content if 'response' in locals() else "No response"}
    except Exception as e:
        return {"error": f"Analysis failed: {str(e)}"}
if __name__ == "__main__":
    pdf_path = r"C:\Users\GOLKAR\Desktop\Reza Golkar-CV.pdf"
    print("Analyzing CV...")
    result = analyze_cv(pdf_path)
    print(json.dumps(result, indent=2, ensure_ascii=False))