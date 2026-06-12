from rag.retrieval import retrieve
from agent.professor_agent import analyze_professor

def analyze_professor_with_rag(query):

    docs = retrieve(query)

    text = "\n".join(
        docs["documents"][0]
    )

    return analyze_professor(text)