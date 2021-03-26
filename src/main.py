from fastapi import FastAPI, Request
from fastapi.params import Depends
from starlette.middleware.base import BaseHTTPMiddleware

from middlewares import processTimeHeader, requestLogging
from routers import employees, redis
from services import elasticService

app = FastAPI()

app.add_middleware(BaseHTTPMiddleware, dispatch=processTimeHeader.add_process_time_header)
app.add_middleware(BaseHTTPMiddleware, dispatch=requestLogging.log_request)
app.include_router(redis.router)
app.include_router(employees.router)

@app.get("/")
async def read_root():
    return {"message": "Hello world!"}

@app.get("/{name}")
async def read_root_with_name(name: str):
    return {"message": f"Hello {name}"}
    