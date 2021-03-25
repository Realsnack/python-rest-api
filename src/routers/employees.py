from fastapi import APIRouter

router = APIRouter(
    prefix="/api/employees",
    tags=["employees"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_employees_root():
    return {"message": "Welcome to employees API"}
