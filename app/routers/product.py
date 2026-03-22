from fastapi import APIRouter
from app.schemas.product import Product
from app.services.product_service import get_product

router = APIRouter()

@router.get("/{product_id}")
def read_user(product_id: int):
    return get_product(product_id)

