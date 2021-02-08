import boto3
import ToDoProperties
from botocore.exceptions import ClientError



def get_todo(id, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url=ToDoProperties.DYNAMODB_URL)

    table = dynamodb.Table(ToDoProperties.TABLE_NAME)

    try:
        response = table.get_item(
            Key={
                'id': id
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response


def main():
    todo = get_todo("123e4567-e89b-12d3-a456-426614174000")
    if todo:
        return todo


if __name__ == '__main__':
    main()