from agent.workflow_v2 import graph

result = graph.invoke(
    {
        "cv_path": r"C:\Users\GOLKAR\Desktop\Reza Golkar-CV.pdf",

        "job_text": """
        PhD Position in Explainable AI and Medical Imaging

        Requirements:
        Python
        PyTorch
        Deep Learning
        Computer Vision
        Medical Image Analysis

        Preferred:
        Explainable AI
        """,

        "professor_text": """
        Research Interests:
        Medical Imaging
        Vision Transformers
        Explainable AI
        Healthcare

        Recent Topics:
        Medical Imaging with Vision Transformers
        Explainable AI methods for healthcare
        """
    }
)

print("\n====================")
print("FINAL REPORT")
print("====================\n")

print(result["report"])