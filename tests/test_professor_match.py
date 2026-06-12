from agent.cv_agent import analyze_cv

from agent.professor_agent import (
    analyze_professor
)

from ml.professor_match import (
    calculate_professor_match
)

cv = analyze_cv(
    r"C:\Users\GOLKAR\Desktop\Reza Golkar-CV.pdf"
)

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

professor = analyze_professor(
    professor_text
)

score = calculate_professor_match(
    cv,
    professor
)

print(
    f"Professor Match: {score}%"
)
