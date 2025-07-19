from pydantic import BaseModel, Field, field_serializer
from decimal import Decimal
from typing import List

class ProductResponse(BaseModel):
    id: str
    name: str
    price: Decimal = Field(...)

    @field_serializer("price")
    def serialize_price(self, price: Decimal) -> float:
        return float(f"{price:.1f}")

class PaginationMeta(BaseModel):
    next: int
    limit: int
    previous: int

class PaginatedResponse(BaseModel):
    data: List[ProductResponse]
    page: PaginationMeta