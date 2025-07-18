from pydantic import BaseModel
from typing import List

class OrderItemModel(BaseModel):
    productId: str
    qty: int

class CreateOrder(BaseModel):
    userId: str
    items: List[OrderItemModel]