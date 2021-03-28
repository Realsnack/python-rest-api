import psycopg2
from fastapi import APIRouter
from pydantic import BaseModel
from services.employeeService import EmployeeService
from typing import Optional

router = APIRouter(
    prefix="/api/employees",
    tags=["employees"],
    responses={404: {"description": "Not found"}},
)

class Employee(BaseModel):
    id: Optional[int]
    name: str
    position: str
    managerId: Optional[int]
    salary: int

employees = EmployeeService()

@router.get("/")
async def read_employees_root():
    pgStatus = employees.get_postgres_status()
    return {"message": "Welcome to employees API", 'isPostgresUp': pgStatus}

@router.post('/new')
async def post_new_employee(employee: Employee):
    return employee
