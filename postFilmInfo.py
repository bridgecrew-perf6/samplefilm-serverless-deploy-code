import json
import os
import logging

import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.getLevelName(os.environ.get('logLevel', 'DEBUG')))
sqsQueueUrl = os.environ['queueUrl']

def send_to_queue(sqsQueueUrl, messageBody):
    isSuccess = False
    try:
        sqsConnection = boto3.client('sqs')
        sqsConnection.send_message(QueueUrl=sqsQueueUrl, MessageBody=messageBody)
        logger.info("Pushed the filmInfo to queue")
        isSuccess = True
    except Exception as err:
        logger.error(f'Failed to send message to queue:{err}')
        isSuccess = False
    return isSuccess



# Lambda handler main function starts here
def postFilmInfo(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    
    print("event", event)
    print("body", event["body"])
    if(send_to_queue(sqsQueueUrl, event["body"])):
        body["success"] = True
    else:
        body["success"] = False
    
    response = {
        "statusCode": 200,
        "headers": {
        "Access-Control-Allow-Origin" : "*"
        },
        "body": json.dumps(body)
    }
    
    return response