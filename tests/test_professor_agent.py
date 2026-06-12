from agent.professor_agent import analyze_professor

professor_text = """
Research interests:

Medical Imaging
Computer Vision
Explainable AI
Vision Transformers

Recent publications:

Vision Foundation Models for Healthcare
Interpretable Deep Learning in Medicine
"""

result = analyze_professor(
    professor_text
)

print(result)