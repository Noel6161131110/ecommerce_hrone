from fastapi.responses import JSONResponse
from fastapi import HTTPException, status

class ProductsController:
    
    def __init__(self):
        pass
    
    async def CreateProducts(
        self,
    ):

        return JSONResponse(
            content={"id": "1234567890"},
            status_code=status.HTTP_201_CREATED
        )

    async def ListProducts(
        self,
    ):

        return {"message": "All products retrieved successfully."}