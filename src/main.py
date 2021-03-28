from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.params import Depends
from starlette.middleware.base import BaseHTTPMiddleware

from middlewares import processTimeHeader, requestLogging
from routers import employees, redis
from services import redisService
from services.employeeService import EmployeeService

app = FastAPI()

app.add_middleware(BaseHTTPMiddleware, dispatch=processTimeHeader.add_process_time_header)
app.add_middleware(BaseHTTPMiddleware, dispatch=requestLogging.log_request)
app.include_router(redis.router)
app.include_router(employees.router)


@app.get("/")
async def read_root():
    return {"message": "Hello world!", 'Time': datetime.now()}


@app.get('/health')
async def read_health():
    redis_status = redisService.get_redis_status()
    employees = EmployeeService()
    employee_status = employees.get_postgres_status()
    return {'redis': redis_status, 'postgresql - employees': employee_status}


@app.get("/{name}")
async def read_root_with_name(name: str):
    return {"message": f"Hello {name}"}
