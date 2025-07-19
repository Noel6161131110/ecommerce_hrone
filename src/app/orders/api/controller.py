from fastapi.responses import JSONResponse
from fastapi import HTTPException, status, Request, Query
from ..models import CreateOrder
from datetime import datetime, timezone
from typing import Optional
from ..schemas import PaginatedResponse
from pymongo import ASCENDING
from bson.decimal128 import Decimal128
from decimal import Decimal
from ..schemas import *
from bson import ObjectId



class OrdersController:
    
    def __init__(self):
        pass

    async def CreateOrders(
        self,
        request: Request,
        order: CreateOrder
    ):
        
        try:
            db = request.app.mongoDb
            
            orderRequest = order.model_dump()
            
            # Currently not checking if the product exist and the stock is available. (SKIPPED)
            
            # userId not required to be checked as it is not used in the current implementation.
            
            # plainly storing the order with the userId and items.
            
            orderRequest["createdAt"] = datetime.now(timezone.utc)
            orderRequest["updatedAt"] = datetime.now(timezone.utc)
            
            result = await db.orders.insert_one(orderRequest)

            return JSONResponse(
                content={
                    "id": str(result.inserted_id)
                },
                status_code=status.HTTP_201_CREATED
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while creating the order: {str(e)}"
            )


    async def ListOfOrders(
        self,
        request: Request,
        user_id: str,
        limit: Optional[int] = Query(10, ge=1),
        offset: Optional[int] = Query(0, ge=0)
    ):
        try:
            db = request.app.mongoDb
            ordersCollection = db.orders
            productsCollection = db.products

            query = {"userId": user_id}
            
            projection = {
                "_id": 1,
                "items": 1
            }

            cursor = ordersCollection.find(query, projection).sort("_id", ASCENDING).skip(offset).limit(limit)

            orders: List[OrderResponse] = []

            async for order in cursor:
                productOrders = []
                total = Decimal("0.0")

                for item in order.get("items", []):
                    productId = item.get("productId")
                    qty = item.get("qty", 0)

                    if not productId:
                        continue

                    product = await productsCollection.find_one(
                        {"_id": ObjectId(productId)},
                        {"_id": 1, "name": 1, "price": 1}  # Only fetching necessary fields / values (that is the projection part)
                    )

                    if not product:
                        continue

                    priceRaw = product.get("price", 0.0)
                    if isinstance(priceRaw, Decimal128):
                        price = priceRaw.to_decimal()
                    elif isinstance(priceRaw, (int, float, str)):
                        price = Decimal(str(priceRaw))
                    else:
                        price = Decimal("0.0")

                    subtotal = price * Decimal(str(qty))
                    total += subtotal

                    productDetail = ProductDetailModel(
                        name=product.get("name", ""),
                        id=str(product["_id"])
                    )

                    productOrders.append(ProductOrderItemModel(
                        productDetails=productDetail,
                        qty=qty
                    ))

                orderResponse = OrderResponse(
                    id=str(order["_id"]),
                    items=productOrders,
                    total=float(total)
                )
                orders.append(orderResponse)

            response = PaginatedResponse(
                data=orders,
                page=PaginationMeta(
                    next=offset + limit,
                    limit=len(orders),
                    previous=max(offset - limit, 0)
                )
            )

            return response

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"An error occurred while retrieving orders: {str(e)}"
            )
