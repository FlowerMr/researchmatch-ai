from sentence_transformers import SentenceTransformer
from rag.chroma_store import collection

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def add_document(text, doc_id):

    embedding = model.encode(text).tolist()

    collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding]
    )