# samplefilm-serverless-deploy-code
samplefilm-serverless-deploy-code


.serverless: This directory will be created when we execute serverless commands and generate cloudformation templates.

buildspec.yaml: This file is used for code build configurations where we install serverless framework and deploy the serverless.yaml file.

postFilmInfo.py: This Lambda function code, takes input from API Gateway and processes it then sends it to SQS Queue.

postFilmInfoDynamo.py: This Lambda function code, takes input from SQS Queue and processes it then stores it in DynamoDB Table.

serverless.yml: This file contains all the above services creation and configuration code.
