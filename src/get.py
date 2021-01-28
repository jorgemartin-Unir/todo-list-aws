import os
import json



def get(event, context):
    # table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # # fetch todo from the database
    # result = table.get_item(
    #     Key={
    #         'id': event['pathParameters']['id']
    #     }
    # )

    # # create a response
    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(result['Item'],
    #                       cls=decimalencoder.DecimalEncoder)
    # }

    # return response
      return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
