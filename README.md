# samplefilm-serverless-deploy-code
samplefilm-serverless-deploy-code


.serverless: This directory will be created when we execute serverless commands and generate cloudformation templates.

buildspec.yaml: This file is used for code build configurations where we install serverless framework and deploy the serverless.yaml file.

postFilmInfo.py: This Lambda function code, takes input from API Gateway and processes it then sends it to SQS Queue.

postFilmInfoDynamo.py: This Lambda function code, takes input from SQS Queue and processes it then stores it in DynamoDB Table.

serverless.yml: This file contains all the above services creation and configuration code.


# serverless.yml

 - Creating API Gateway and SQS. Keeping API Gateway and SQS as an event and environment variables respectively for SampleFilmInfo Lambda function.
 - SampleFilmInfo  Lambda function gets user inputs from API Gateway invoke URL, process it and send it to SQS.
 - Using SQS as an event to the next Lambda function PostFilmInfoToDynamo 
 - PostFilmInfoToDynamo  Lambda function processes the event and stores the details in DynamoDB.

If you would like to play with serverless framework, follow the below steps.

To install the Serverless Framework click [here](https://www.serverless.com/framework/docs/getting-started), follow the instructions provided in the mentioned link.

# Serverless Framework Commands:-

- serverless create --template aws-python3
- serverless config credentials --provider aws --key YOUR-KEY --secret YOUR-SECRET
- serverless package –aws-profile *******
- serverless deploy –aws-profile ********

