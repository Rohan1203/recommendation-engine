from fastapi import APIRouter
from app.services.product_service import recommend_products

router = APIRouter()

@router.get("/{user_id}")
def get_recommendations(user_id: int):
    return recommend_products(user_id)