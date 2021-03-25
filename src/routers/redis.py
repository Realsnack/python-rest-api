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


def get_redis_status():
    try:
        pingResult = r.ping()
    except:
        pingResult = False
    return pingResult


@router.get("/")
async def read_redis_root():
    redis_status = get_redis_status()
    return {"message": "Welcome to Redis API", 'isRedisUp': redis_status}


@router.get('/{key}')
async def read_redis_key(key: str):
    value = r.get(key)
    return {'Key': key, 'Value': value}
