import json
import time

from fastapi import Request
from services.elasticService import ElasticService

elastic = ElasticService()


async def log_request(request: Request, call_next):
    headers = request.headers
    body = None
    path = str(request.url)
    method = request.method

    # if (method == 'PUT' or method == 'POST'):
    #     body = await request.json()

    response = await call_next(request)
    statusCode = response.status_code

    if (body == None):
        elastic.index_request(method, path, statusCode, headers)
        return response

    elastic.index_request(method, path, statusCode, headers, str(body))

    return response
