from fastapi import APIRouter
from app.services.rag_pipeline import get_answer

router = APIRouter()

@router.get("/ask")
def ask(query: str):
    return {"response": get_answer(query)}