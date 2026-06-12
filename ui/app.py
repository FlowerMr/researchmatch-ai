import streamlit as st
import requests

st.title(
    "ResearchMatch AI"
)

cv_path = st.text_input(
    "CV Path"
)

job_text = st.text_area(
    "Job Description"
)

professor_text = st.text_area(
    "Professor Profile"
)

if st.button("Analyze"):

    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        params={
            "cv_path": cv_path,
            "job_text": job_text,
            "professor_text": professor_text
        }
    )

    st.json(
        response.json()
    )