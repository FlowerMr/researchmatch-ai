import requests

response = requests.post(
    "http://127.0.0.1:8000/analyze",
    params={
        "cv_path":
        r"C:\Users\GOLKAR\Desktop\Reza Golkar-CV.pdf",

        "job_text":
        "PhD Position in Explainable AI",

        "professor_text":
        "Research Interests: Medical Imaging"
    }
)

print(response.json())