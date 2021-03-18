from fastapi import APIRouter

router = APIRouter(
    prefix="/api/redis",
    tags=["redis"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_redis_root():
    return {"message": "Welcome to Redis API"}
