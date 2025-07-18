from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.database.db import *
from src.app.routes import router as Router
from dotenv import load_dotenv
import os, sys, uvicorn, asyncio

sys.dont_write_bytecode = True

load_dotenv()

IS_PRODUCTION = os.getenv("ENV_MODE") == "PRODUCTION"



@asynccontextmanager
async def lifespan(app : FastAPI):
    # await initDB()

    yield


app = FastAPI(
    lifespan=lifespan,
    title="Ecommerce Backend Service",
    version="v1",
    description="Backend service for the Ecommerce application.",
    docs_url=None if IS_PRODUCTION else "/docs",
    redoc_url=None if IS_PRODUCTION else "/redoc",  
    )


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

app.include_router(Router, prefix="")

async def main():
    config = uvicorn.Config(app, host='0.0.0.0')
    server = uvicorn.Server(config)

    await server.serve()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped by user interaction.")