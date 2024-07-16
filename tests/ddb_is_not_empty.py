import json
import boto3
import os
import pytest



def test_DynamoDB_Not_Empty():
    region_name = os.environ["REGION"]
    table_name = os.environ["TABLE_NAME"]
    try:
        client = boto3.client('dynamodb',  region_name=region_name)
        res = client.get_item(
            TableName=table_name,
            Key={
                'website':{
                    'S': 'germansp.com'
                }
            }
        )
        
        try:
            assert "Item" in res
        except AssertionError as e:
            raise Exception("The table is not populated, so no items were returned. Make sure it has items") from e
    except:
        raise Exception("No resource was found")
