from rag.ingest import add_document

paper = """
Medical Imaging with Vision Transformers.
Explainable AI methods for healthcare.
"""

add_document(
    paper,
    "paper1"
)

print("stored")