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


def set(key: str, value: str):
    try:
        r.set(key, value)
        return True
    except:
        print()
        return False


def get_count(pattern: str = None):
    # Add wildcards to the pattern
    if (pattern == None):
        pattern = '*'
    else:
        pattern = f'*{pattern}*'

    print(f'Pattern {pattern}')
    _cursor = 0
    keys_count = 0
    while (True):
        scan_result = r.scan(cursor=_cursor, match=pattern)
        _cursor = scan_result[0]
        keys_count += len(scan_result[1])

        if(_cursor == 0):
            return keys_count
