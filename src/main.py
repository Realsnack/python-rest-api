from fastapi import FastAPI
from fastapi.params import Depends
from routers import redis

app = FastAPI()

app.include_router(redis.router)

@app.get("/")
async def read_root():
    return {"message": "Hello world!"}

@app.get("/{name}")
async def read_root_with_name(name: str):
    return {"message": f"Hello {name}"}