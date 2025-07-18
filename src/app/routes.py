from fastapi import APIRouter
from src.app.orders.routes import router as orderRouter
from src.app.products.routes import router as productRouter

router = APIRouter()

router.include_router(orderRouter, prefix="/orders", tags=["Orders"])
router.include_router(productRouter, prefix="/products", tags=["Products"])

