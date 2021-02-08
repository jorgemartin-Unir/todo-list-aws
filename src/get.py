import os
import json
import boto3
import decimalencoder
import properties

dynamodb = boto3.resource('dynamodb')

def get(event, context):
  table = dynamodb.Table("todoTable_B")

  # fetch todo from the database
  result = table.get_item(
    Key={
        'id': event['pathParameters']['id']
        }
  )

  # create a response
  response = {
    "statusCode": 200,
      "body": json.dumps(result['Item'],
        cls=decimalencoder.DecimalEncoder)
    
  }
  # return response
  return response
