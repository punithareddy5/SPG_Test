import json
import uuid
import boto3

def lambda_handler(event, context):
    # TODO implement
    body = json.loads(event['body'])
    number = body['number']
    message = body['message']
    output = {"number": number, "message": message, "request_id": str(uuid.uuid1())}
    json_dump = json.dumps(output)

    
    sns_client = boto3.client('sns')
    aws_account_id = context.invoked_function_arn.split(":")[4]
    aws_region = context.invoked_function_arn.split(":")[3]
    response = sns_client.publish(
    TopicArn='arn:aws:sns:{0}:{1}:SendSMSTopic'.format(aws_region, aws_account_id),
    Message= json_dump
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "Details": "Message being processed...",
            "number": number,
            "message": message,
            "unique request id": str(uuid.uuid1())
        })
    }