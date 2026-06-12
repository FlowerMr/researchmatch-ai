from agent.cv_agent import analyze_cv
from agent.position_agent import analyze_position

from ml.match_engine import calculate_match


cv = analyze_cv(
    r"C:\Users\GOLKAR\Desktop\Reza Golkar-CV.pdf"
)

job_text = """
PhD Position in Explainable AI and Medical Imaging

Requirements:

Python
Deep Learning
PyTorch
Computer Vision
Medical Imaging

Preferred:

Explainable AI

Research Area:

Healthcare AI
"""

position = analyze_position(job_text)

score = calculate_match(
    cv,
    position
)

print(f"Match Score: {score}%")