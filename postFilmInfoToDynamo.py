import json
import os
import logging

import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.getLevelName(os.environ.get('logLevel', 'DEBUG')))
dynamoDBTable = os.environ['DynamoTable']

dynamodb = boto3.resource('dynamodb')

# Lambda handler main function starts here
def saveFilmInfoDynamo(event, context):
    print("event = ", event)
    print("dynamoDBTable = ", dynamoDBTable)
    table = dynamodb.Table(dynamoDBTable)
    print("table = ", table)
    filmDetailsInfo = json.loads(event['Records'][0]['body'])
    print("filmDetailsInfo = ",filmDetailsInfo)
    print("type of filmDetailsInfo = ", type(filmDetailsInfo))
    try:
        item  = {
            'FilmTitle': filmDetailsInfo['shortFilmTitle'],
            'Caption': filmDetailsInfo['Caption'],
            'Director': filmDetailsInfo['Director'],
            'Producer': filmDetailsInfo['Producer'],
            'Theme': filmDetailsInfo['Theme'],
            'Jhonor': filmDetailsInfo['Jhonor'],
            'MobileNo': int(filmDetailsInfo['Mobile'])
            }
        table.put_item(Item=item)
    except Exception as err:
        logger.error(f'Failed to post message to dynamo table:{err}')