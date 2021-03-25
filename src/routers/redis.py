from fastapi import APIRouter
from services import redisService

router = APIRouter(
    prefix="/api/redis",
    tags=["redis"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def read_redis_root():
    redis_status = redisService.get_redis_status()
    return {"message": "Welcome to Redis API", 'isRedisUp': redis_status}


@router.get('/{key}')
async def read_redis_key(key: str):
    value = redisService.get(key)
    return {'Key': key, 'Value': value}