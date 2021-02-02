import boto3
import urllib
import os
import requests
from requests_aws4auth import AWS4Auth

region      = os.environ["AWS_REGION"]
service     = "es"
credentials = boto3.Session().get_credentials()
awsauth     = AWS4Auth(credentials.access_key,
                   credentials.secret_key,
                   region,
                   service,
                   session_token=credentials.token)

elastic_search_host = os.environ["ELASTIC_SEARCH_HOST"]
index               = "documents"
type                = "doc"
headers             = {"Content-Type": "application/json"}
elastic_url         = elastic_search_host + index + '/' + type


class DocumentIndexer():
    
    def index(self, document):
        # Index the full document (pages and entities) in elasticsearch:

        response = requests.post(elastic_url,
                                 auth=awsauth,
                                 json=document,
                                 headers=headers)
        response.raise_for_status()

        es_response = response.json()
        return es_response["_id"]