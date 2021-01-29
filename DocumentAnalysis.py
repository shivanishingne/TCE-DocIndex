import json
import boto3

textract = boto3.client('textract')


def lambda_handler(event, context):
    
    message = json.loads(event['Records'][0]['Sns']['Message'])

    jobId = message['JobId']
    print("JobId="+jobId)

    status = message['Status']
    print("Status="+status)

    if status != "SUCCEEDED":
        return {
            # TODO : for DLQ - https://docs.aws.amazon.com/lambda/latest/dg/dlq.html
            "status": status
        }

    result = textract.get_document_text_detection(  # to get the textract result
        JobId=jobId
    )

    print(result)