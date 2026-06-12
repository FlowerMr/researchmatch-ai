from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def calculate_professor_match(
    cv_data,
    professor_data
):

    cv_text = " ".join(
        cv_data.get("skills", [])
        + cv_data.get("research_interests", [])
        + cv_data.get("projects", [])
    )

    professor_text = " ".join(
        professor_data.get("Research Interests", [])
        + professor_data.get("Recent Topics", [])
        + professor_data.get("Keywords", [])
    )

    cv_embedding = model.encode([cv_text])

    professor_embedding = model.encode(
        [professor_text]
    )




    similarity = cosine_similarity(
        cv_embedding,
        professor_embedding
    )[0][0]
    
    return float(round(similarity * 100, 2))