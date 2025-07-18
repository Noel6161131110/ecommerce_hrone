from pymongo import AsyncMongoClient
from dotenv import load_dotenv
import os, asyncio
from fastapi import FastAPI

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = AsyncMongoClient(MONGODB_URI)

async def initDBClient(app: FastAPI):
    try:
        app.mongoDbClient = AsyncMongoClient(MONGODB_URI)
        
        app.mongoDb = app.mongoDbClient.get_database("ecommerce_hrone")

        print("Connected successfully")

    except Exception as e:
        raise Exception("The following error occurred: ", e)



async def closeDBClient(app: FastAPI):
    await app.mongoDbClient.close()
    
    print("Database connection closed successfully")