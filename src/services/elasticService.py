from elasticsearch import Elasticsearch
from datetime import datetime
from services import configurationService
import json


class ElasticService:
    def __init__(self):
        self.elasticHost = configurationService.config['Elasticsearch']['Hosts']
        self.es = Elasticsearch(self.elasticHost)

    def indexDocument(self, document):
        # document.update('timestamp': datetime.now())
        self.es.index(index='python-api-logs', body=document)

    def indexRequest(self, method: str, url: str, status_code: int, headers: {}, body: str = None):
        document = self.__createDocument__(body, method, url, status_code)

        self.__add_headers__(document, headers)
        document.update({'timestamp': datetime.now()})
        self.es.index(index='python-api-logs', body=document)

    def __createDocument__(self, body, method, url, status_code):
        if (body == None):
            document = {
                'method': method,
                'url': url,
                'status_code': status_code
            }
        elif (body != None):
            document = {
                'method': method,
                'url': url,
                'status_code': status_code,
                'body': body
            }
        return document

    def __add_headers__(self, document, headers):
        for header in headers:
            document.update({f'header.{header}': headers.get(header)})

        return document
