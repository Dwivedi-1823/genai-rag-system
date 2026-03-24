import os
from app.utils.chunking import split_text
from app.services.embeddings import get_embeddings
from langchain_community.vectorstores import Chroma
import chromadb

DATA_PATH = "data/sample.txt"
PERSIST_DIR = "vectorstore"

def ingest():
    # 1. Read and Chunk
    if not os.path.exists(DATA_PATH):
        print(f"Error: {DATA_PATH} not found.")
        return

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        text = f.read()
    chunks = split_text(text)

    # 2. Get your specific embedding model
    embeddings = get_embeddings()

    # 3. Use PersistentClient instead of the generic Client
    # This avoids the "Settings" overhead and is the modern Chroma standard
    client = chromadb.PersistentClient(path=PERSIST_DIR)

    # 4. Initialize LangChain's Chroma wrapper
    # We pass the client AND the embedding function here
    db = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        client=client,
        collection_name="rag_collection"
    )

    # Note: db.persist() is deprecated in newer Chroma versions 
    # as PersistentClient handles it automatically, but it doesn't hurt.
    print(f"Ingestion completed! {len(chunks)} chunks added.")

if __name__ == "__main__":
    ingest()