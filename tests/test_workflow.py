from agent.workflow import app

job_text = """
PhD Position in Explainable AI and Medical Imaging

Requirements:

Python
PyTorch
Deep Learning
Computer Vision
Medical Image Analysis

Preferred:
Explainable AI
"""

result = app.invoke(
    {
        "cv_path": r"C:\Users\GOLKAR\Desktop\Reza Golkar-CV.pdf",
        "job_text": job_text
    }
)

print(result)