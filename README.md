# ResearchMatch AI

ResearchMatch AI is a multi-agent AI platform designed to help students, researchers, and PhD applicants evaluate their compatibility with research positions and academic supervisors.

The system automatically analyzes a candidate's CV, extracts key skills and research interests, compares them with PhD/job descriptions and professor profiles, identifies skill gaps, and generates personalized recommendations for improving application success.

---

## Features

### CV Analysis Agent

* Extracts text from PDF resumes
* Identifies:

  * Skills
  * Education
  * Projects
  * Research Interests

### Position Analysis Agent

* Analyzes PhD/job descriptions
* Extracts:

  * Required Skills
  * Research Topics
  * Preferred Qualifications
  * Keywords

### Professor Analysis Agent

* Extracts:

  * Research Interests
  * Recent Research Topics
  * Academic Keywords

### Semantic Matching Engine

* Computes similarity between:

  * Candidate CV ↔ Position
  * Candidate CV ↔ Professor

### Gap Analysis

* Detects:

  * Missing Skills
  * Matched Skills
  * Research Alignment Gaps

### Recommendation Agent

* Generates personalized suggestions to improve applications.

### Critic Agent

* Reviews the application critically.
* Identifies weaknesses and missing qualifications.

### Report Generator

* Produces a structured final report.

### Workflow Orchestration

* Multi-agent pipeline powered by LangGraph.

### Database Storage

* Stores generated reports in SQLite.

### REST API

* FastAPI backend for external integrations.

### Dashboard

* Streamlit-based user interface.

---

# System Architecture

CV PDF
↓
CV Agent
↓
Position Agent
↓
Professor Agent
↓
Match Engine
↓
Gap Analyzer
↓
Recommendation Agent
↓
Critic Agent
↓
Report Agent
↓
SQLite Storage
↓
Dashboard

---

# Technologies Used

## Artificial Intelligence

* Large Language Models (LLMs)
* Prompt Engineering
* Semantic Search
* Retrieval-Augmented Reasoning
* Multi-Agent Systems

## Machine Learning

* Sentence Transformers
* Embedding-Based Similarity
* Cosine Similarity

## NLP

* Information Extraction
* Keyword Extraction
* Research Topic Mining
* Skill Extraction

## Python Libraries

### LLM Frameworks

* LangChain
* LangGraph
* Google Generative AI

### Embeddings

* sentence-transformers
* all-MiniLM-L6-v2

### Machine Learning

* scikit-learn
* NumPy
* SciPy

### PDF Processing

* PyMuPDF (fitz)

### Backend

* FastAPI
* Uvicorn
* Pydantic

### Database

* SQLite3

### Frontend

* Streamlit

### Utilities

* python-dotenv
* requests
* json

---

# Project Structure

```text
researchmatch-ai/

├── agent/
│   ├── cv_agent.py
│   ├── position_agent.py
│   ├── professor_agent.py
│   ├── recommendation_agent.py
│   ├── critic_agent.py
│   ├── report_agent.py
│   ├── storage_agent.py
│   └── workflow_v2.py
│
├── ml/
│   ├── match_engine.py
│   ├── gap_analyzer.py
│   └── professor_match.py
│
├── database/
│   ├── db.py
│   └── history.py
│
├── api/
│   └── main.py
│
├── dashboard/
│   └── app.py
│
├── tests/
│
├── researchmatch.db
│
└── requirements.txt
```

---

# Example Output

```json
{
  "match_score": 67.1,
  "professor_match": 64.8,
  "matched_skills": [
    "PyTorch",
    "Deep Learning",
    "Computer Vision"
  ],
  "missing_skills": [
    "Medical Image Analysis"
  ],
  "recommendation": "...",
  "critique": "..."
}
```

---

# Future Improvements

* Multi-professor ranking
* Automatic university crawling
* Research paper retrieval
* RAG-based professor profiling
* Email generation for faculty outreach
* PhD application scoring
* Docker deployment
* Cloud deployment (AWS/Azure/GCP)
* Vector databases (ChromaDB)
* Authentication system

---

# Author

Reza Golkar

M.Sc. Artificial Intelligence

Research Interests:

* Explainable AI (XAI)
* Computer Vision
* Medical Image Analysis
* Multi-Agent Systems
* Large Language Models
* Retrieval-Augmented Generation (RAG)
<img width="1904" height="708" alt="image" src="https://github.com/user-attachments/assets/8dcfac3c-c84b-4cb0-a5ea-6b6ed45aab12" />

