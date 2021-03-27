from fastapi import APIRouter
from pydantic import BaseModel
import redis
from services import redisService

router = APIRouter(
    prefix="/api/redis",
    tags=["redis"],
    responses={404: {"description": "Not found"}},
)


class RedisKey(BaseModel):
    Key: str
    Value: str


@router.get("/")
async def read_redis_root():
    redis_status = redisService.get_redis_status()
    return {"message": "Welcome to Redis API", 'isRedisUp': redis_status}


@router.get('/{key}')
async def read_redis_key(key: str):
    value = redisService.get(key)
    return {'key': key, 'value': value}


@router.post('/set')
async def create_redis_key(redis_key: RedisKey):
    if (redisService.set(redis_key.Key, redis_key.Value)):
        return redis_key

    return {"message": f"Key {redis_key.Key} wasn't created because of an error"}
