from typing import Dict
from elasticsearch import Elasticsearch
from datetime import datetime
from services import configurationService
import json


class ElasticService:
    def __init__(self):
        self._elastic_host = configurationService.config['Elasticsearch']['Hosts']
        self.es = Elasticsearch(self._elastic_host)

    def index_document(self, document):
        # document.update('timestamp': datetime.now())
        self.es.index(index='python-api-logs', body=document)

    def index_request(self, method: str, url: str, status_code: int, headers: Dict[str, str], body: str = None):
        document = self.__create_document__(body, method, url, status_code)

        self.__add_headers__(document, headers)
        document.update({'timestamp': datetime.now()})
        self.es.index(index='python-api-logs', body=document)

    def __create_document__(self, body, method, url, status_code):
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
