from fastapi import FastAPI
from pydantic import BaseModel
from agent.workflow_v2 import graph

app = FastAPI()


class AnalyzeRequest(BaseModel):
    cv_path: str
    job_text: str
    professor_text: str


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/analyze")
def analyze(req: AnalyzeRequest):

    result = graph.invoke(
        {
            "cv_path": req.cv_path,
            "job_text": req.job_text,
            "professor_text": req.professor_text
        }
    )

    return result