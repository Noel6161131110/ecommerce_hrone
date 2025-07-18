from src.app.orders.api.controller import *
from fastapi import APIRouter

router = APIRouter()

orderController = OrdersController()

routes = [
    {
        "path": "/{user_id}",
        "endpoint": orderController.ListOfOrders,
        "method": "GET",
        "name": "List Of Orders"
    },
    {
        "path": "",
        "endpoint": orderController.CreateOrders,
        "method": "POST",
        "name": "Create Order"
    }
]

for route in routes:
    router.add_api_route(
        path=route["path"], 
        endpoint=route["endpoint"], 
        methods=[route["method"]], 
        name=route["name"]
    )