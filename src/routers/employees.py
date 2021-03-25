from fastapi import APIRouter
from services.employeeService import EmployeeService
import psycopg2

router = APIRouter(
    prefix="/api/employees",
    tags=["employees"],
    responses={404: {"description": "Not found"}},
)

employees = EmployeeService()

@router.get("/")
async def read_employees_root():
    pgStatus = employees.get_postgres_status()
    return {"message": "Welcome to employees API", 'isPostgresUp': pgStatus}
