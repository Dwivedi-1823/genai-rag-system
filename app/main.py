from fastapi import FastAPI
from app.routes.qa import router

app = FastAPI(title="GenAI RAG System")

app.include_router(router)