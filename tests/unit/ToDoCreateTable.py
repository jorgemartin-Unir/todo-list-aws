import boto3
import ToDoProperties


def create_todo_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=ToDoProperties.DYNAMODB_URL)
        

    table = dynamodb.create_table(
        TableName=ToDoProperties.TABLE_NAME,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName=ToDoProperties.TABLE_NAME)
    if (table.table_status != 'ACTIVE'):
        raise AssertionError()

    return table


if __name__ == '__main__':
    print("Table status:", create_todo_table().table_status)