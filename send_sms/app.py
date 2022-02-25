import json
import uuid
import boto3

def lambda_handler(event, context):
    # TODO implement
    # print (event)
    body = json.loads(event['Records'][0]['body'])
    Message = body['Message']
    Message_loads = json.loads(Message)

    number = Message_loads['number']
    message = Message_loads['message']
    
    print (number)
    
    sns_client = boto3.client('sns')
    aws_account_id = context.invoked_function_arn.split(":")[4]
    aws_region = context.invoked_function_arn.split(":")[3]
    response = sns_client.publish(
    PhoneNumber= number,
    Message= message
    )
    
    print (response)
