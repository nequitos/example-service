
from uvicorn import Config, Server

from fastapi import FastAPI
from src.routers import *


app = FastAPI()
app.include_router(order_router)


async def main():
    config = Config("app:app", host="0.0.0.0", port=80, log_level="debug")
    server = Server(config)

    return await server.serve()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())