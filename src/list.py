import json
import os
import boto3
import decimalencoder
import properties

dynamodb = boto3.resource('dynamodb')


def list(event, context):
    table = dynamodb.Table("todoTable_B")

    # fetch all todos from the database
    result = table.scan()

    # create a response
    response = {
     "statusCode": 200,
     "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response
