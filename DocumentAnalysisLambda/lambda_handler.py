import json
from text_extractor import TextExtractor
from document_analyzer import DocumentAnalyzer

text_extractor = TextExtractor()
document_analyzer = DocumentAnalyzer()


def lambda_handler(event, context):
    
    message = json.loads(event['Records'][0]['Sns']['Message'])

    jobId   = message['JobId']
    print("JobId="+jobId)

    status  = message['Status']
    print("Status="+status)
    if status != "SUCCEEDED":
        return {
            # TODO : for DLQ - https://docs.aws.amazon.com/lambda/latest/dg/dlq.html
            "status": status
        }

    pages   = text_extractor.extract_text(jobId)
    print(list(pages.values()))
    
    entities = document_analyzer.extract_entities(list(pages.values()))
    print(entities)
    