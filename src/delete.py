import os
import boto3
import properties



dynamodb = boto3.resource('dynamodb')


def delete(event, context):
    table = dynamodb.Table(properties.TABLE_NAME)

    # delete the todo from the database
    table.delete_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200
    }

    return response
