from fastapi.responses import JSONResponse
from fastapi import HTTPException, status, Request, Query
from ..models import CreateProduct
from datetime import datetime, timezone
from typing import Optional
from pymongo import ASCENDING
from bson.decimal128 import Decimal128
from decimal import Decimal
from ..schemas import ProductResponse, PaginatedResponse, PaginationMeta
from fastapi.encoders import jsonable_encoder
class ProductsController:
    
    def __init__(self):
        pass
    
    async def CreateProducts(
        self,
        request: Request,
        product: CreateProduct
    ):
        try:
            db = request.app.mongoDb
            
            currentTime = datetime.now(timezone.utc)
            
            productRequest = product.model_dump()
            
            productRequest["price"] = Decimal128(productRequest['price'])
            productRequest["createdAt"] = currentTime
            productRequest["updatedAt"] = currentTime
            
            result = await db.products.insert_one(productRequest)

            return JSONResponse(
                content={
                    "id": str(result.inserted_id)
                },
                status_code=status.HTTP_201_CREATED
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while creating the product: {str(e)}"
            )

    async def ListProducts(
        self,
        request: Request,
        name: Optional[str] = None,
        size: Optional[str] = None,
        limit: Optional[int] = Query(10, ge=1),
        offset: Optional[int] = Query(0, ge=0)
    ):
        try:
            db = request.app.mongoDb
            collection = db.products
            
            query = {}
            
            if name:
                query["name"] = {"$regex": name, "$options": "i"}
            if size:
                query["sizes.size"] = size
                
            projection = {
                "_id": 1,
                "name": 1,
                "price": 1,
            }

            cursor = collection.find(query, projection).sort("_id", ASCENDING).skip(offset).limit(limit)

            products = []
            
            async for product in cursor:
        
                price = product.get("price", Decimal128("0.0"))
                
                if isinstance(price, Decimal128):
                    price = float(f"{price.to_decimal():.1f}")

                products.append({
                    "id": str(product["_id"]),
                    "name": product.get("name", ""),
                    "price": price
                })

            return JSONResponse(
                content=jsonable_encoder(PaginatedResponse(
                    data = [ProductResponse(**p) for p in products],
                    page = PaginationMeta(
                        next=offset + limit,
                        imit=len(products),
                        previous=max(offset - limit, 0)
                    )
                )),
                status_code=status.HTTP_200_OK
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while retrieving the products: {str(e)}"
            )