from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def calculate_match(cv_data, position_data):

    cv_text = " ".join(
        cv_data.get("skills", [])
        + cv_data.get("research_interests", [])
        + cv_data.get("projects", [])
    )

    position_text = " ".join(
        position_data.get("required_skills", [])
        + position_data.get("research_topics", [])
        + position_data.get("keywords", [])
    )

    cv_embedding = model.encode([cv_text])

    position_embedding = model.encode([position_text])

    score = cosine_similarity(
        cv_embedding,
        position_embedding
    )[0][0]

    return round(float(score) * 100, 2)