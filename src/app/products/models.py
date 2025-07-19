from pydantic import BaseModel, Field, field_validator
from typing import List
from decimal import Decimal, ROUND_DOWN

class SizeModel(BaseModel):
    size: str
    quantity: int

class CreateProduct(BaseModel):
    name: str
    price: Decimal = Field(...)
    sizes: List[SizeModel]

    @field_validator("price", mode="before")
    def ensure_decimal_format(cls, v):
        try:
            return Decimal(v).quantize(Decimal("0.1"), rounding=ROUND_DOWN)
        except Exception as e:
            raise ValueError("Invalid decimal format for price")