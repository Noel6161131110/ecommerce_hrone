from pydantic import BaseModel, Field, field_serializer
from decimal import Decimal
from typing import List

class ProductDetailModel(BaseModel):
    name: str
    id: str

class ProductOrderItemModel(BaseModel):
    productDetails: ProductDetailModel
    qty: int

class OrderResponse(BaseModel):
    id: str
    items: List[ProductOrderItemModel]
    total: float = Field(...)

    @field_serializer("total")
    def serialize_total(self, value: float) -> float:
        return float(f"{value:.1f}") 

class PaginationMeta(BaseModel):
    next: int
    limit: int
    previous: int

class PaginatedResponse(BaseModel):
    data: List[OrderResponse]
    page: PaginationMeta