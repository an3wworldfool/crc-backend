import json
import boto3
import botocore
import os

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    print(os.environ['DYNAMODB_TABLE'])
    response = ""
    try:
        response = client.update_item(
        ExpressionAttributeNames={
            '#v': 'views',
        },
        ExpressionAttributeValues={
            ':c': {
                'N': '1',
            },
            },
        Key={
            'website': {
                'S': 'germansp.com',
            }
        },
        ReturnValues='UPDATED_NEW',
        TableName=os.environ['DYNAMODB_TABLE'],
        UpdateExpression='SET #v = #v + :c',
        )
    except botocore.exceptions.ClientError as error:
        # Put your error handling logic here
        raise error
    
    except botocore.exceptions.ParamValidationError as error:
        raise ValueError('The parameters you provided are incorrect: {}'.format(error))
    except:
        print("there was an error with DynamoDB req")

    
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Headers": 'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token',
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,GET"
        },
        'body': json.dumps({"views":response["Attributes"]["views"]["N"]})
    }


