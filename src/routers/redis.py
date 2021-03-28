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
    key: str
    value: str


@router.get("/")
async def read_redis_root():
    redis_status = redisService.get_redis_status()
    return {"message": "Welcome to Redis API", 'isRedisUp': redis_status}


@router.get('/count')
async def count_redis_keys():
    key_count = redisService.get_count()

    return {'pattern': '*', 'count': key_count}

@router.get('/count/{pattern}')
async def count_redis_keys(pattern: str):
    key_count = redisService.get_count(pattern)

    return {'pattern': pattern, 'count': key_count}


@router.post('/set')
async def create_redis_key(redis_key: RedisKey):
    if (redisService.set(redis_key.key, redis_key.value)):
        return redis_key

    return {"message": f"Key {redis_key.key} wasn't created because of an error"}


@router.get('/{key}')
async def read_redis_key(key: str):
    value = redisService.get(key)
    return {'key': key, 'value': value}
