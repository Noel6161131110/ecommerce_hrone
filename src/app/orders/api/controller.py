from fastapi.responses import JSONResponse
from fastapi import HTTPException, status


class OrdersController:
    
    def __init__(self):
        pass

    async def CreateOrders(
        self,
    ):

        return JSONResponse(
            content={"id": "1234567890"},
            status_code=status.HTTP_201_CREATED
        )
    async def ListOfOrders(
        self,
    ):

        return {"message": "All orders retrieved successfully."}
