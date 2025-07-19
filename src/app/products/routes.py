from src.app.products.api.controller import *
from fastapi import APIRouter
from .schemas import PaginatedResponse

router = APIRouter()

productsController = ProductsController()

routes = [
    {
        "path": "",
        "endpoint": productsController.ListProducts,
        "method": "GET",
        "name": "List Products",
        "response_model": PaginatedResponse
    },
    {
        "path": "",
        "endpoint": productsController.CreateProducts,
        "method": "POST",
        "name": "Create Product"
    }
]

for route in routes:
    router.add_api_route(
        path=route["path"],
        endpoint=route["endpoint"],
        methods=[route["method"]],
        name=route["name"],
        response_model=route.get("response_model")
    )