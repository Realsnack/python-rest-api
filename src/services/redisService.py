import redis

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

def get(key: str):
    value = r.get(key)
    return value