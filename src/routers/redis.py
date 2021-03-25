from fastapi import APIRouter
import redis

router = APIRouter(
    prefix="/api/redis",
    tags=["redis"],
    responses={404: {"description": "Not found"}},
)

r = redis.Redis(
    host='192.168.1.27',
    port=6379
)


@router.get("/")
async def read_redis_root():
    return {"message": "Welcome to Redis API"}


@router.get('/{key}')
async def read_redis_key(key: str):
    value = r.get(key)
    return {'Key': key, 'Value': value}
