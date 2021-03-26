from elasticsearch import Elasticsearch
from datetime import datetime
from services import configurationService

class ElasticService:
    def __init__(self):
        self.elasticHost = configurationService.config['Elasticsearch']['Hosts']
        self.es = Elasticsearch(self.elasticHost)

    def indexDocument(self, document):
        self.es.index(index='python-api-logs', body=document)