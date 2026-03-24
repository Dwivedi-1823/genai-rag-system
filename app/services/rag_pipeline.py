from langchain_community.vectorstores import Chroma
from app.services.embeddings import get_embeddings
from app.services.llm import get_llm_response

PERSIST_DIR = "vectorstore"

def get_answer(query: str):
    db = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=get_embeddings(),
        collection_name="rag_collection"
    )

    docs = db.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer only from the context below.

Context:
{context}

Question:
{query}
"""

    response = get_llm_response(prompt)
    return response