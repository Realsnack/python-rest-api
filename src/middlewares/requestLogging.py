import json
import time

from fastapi import Request
from services.elasticService import ElasticService

elastic = ElasticService()


async def log_request(request: Request, call_next):
    headers = request.headers

    method = request.method
    if (method == 'PUT' or method == 'POST'):
        body = await request.body()

    response = await call_next(request)
    statusCode = response.status_code

    if (method == 'PUT' or method == 'POST'):
        document = {
            'headers': str(headers),
            'method': method,
            'body': str(body),
            'status_code': statusCode
        }
    else:
        document = {
            'headers': str(headers),
            'method': method,
            'status_code': statusCode
        }

    elastic.indexDocument(document)

    return response
