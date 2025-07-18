from pymongo import AsyncMongoClient
from dotenv import load_dotenv
import os, asyncio

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = AsyncMongoClient(MONGODB_URI)

async def initDB():
    try:

        await client.admin.command("ping")
        print("Connected successfully")

        await client.close()
    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)


async def getSession():
    database = client['ecommerce_hrone']
    
    return database