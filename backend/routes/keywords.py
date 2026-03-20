from fastapi import APIRouter
from database import keyword_collection

router = APIRouter()

@router.post("/add-keyword")
def add_keyword(keyword: str):
    keyword_collection.insert_one({"keyword": keyword})
    return {"message": "Keyword added"}

@router.get("/keywords")
def get_keywords():
    return list(keyword_collection.find({}, {"_id": 0}))