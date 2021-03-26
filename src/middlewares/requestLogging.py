import time
import json

from fastapi import Request


async def log_request(request: Request, call_next):
    # headerDict = {}
    headers = request.headers
    for header in headers:
        print(f'Header: {header}: {headers.get(header)}')

    method = request.method
    if (method == 'PUT' or method == 'POST'):
        body = await request.body()
        print(f'Body: {body}')

    response = await call_next(request)
    print(f'Status: {response.status_code}')

    return response
