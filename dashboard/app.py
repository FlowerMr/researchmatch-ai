import streamlit as st
import requests

st.title("ResearchMatch AI")

cv_path = st.text_input(
    "CV Path"
)

job_text = st.text_area(
    "PhD Position"
)

professor_text = st.text_area(
    "Professor Profile"
)

analyze_btn = st.button(
    "Analyze"
)
if analyze_btn:

    payload = {
        "cv_path": cv_path,
        "job_text": job_text,
        "professor_text": professor_text
    }

    response = requests.post(
        "http://127.0.0.1:9000/analyze",
        json=payload
    )

    st.json(
        response.json()
    )