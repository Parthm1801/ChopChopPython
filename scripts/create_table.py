# import boto3
#
# dynamodb = boto3.client(
#     "dynamodb",
#     region_name="us-east-1",
#     endpoint_url="http://localhost:8000",
#     aws_access_key_id="dummy",
#     aws_secret_access_key="dummy"
# )
#
# dynamodb.create_table(
#     TableName="chopchop_goals",
#     KeySchema=[
#         {"AttributeName": "user_id", "KeyType": "HASH"},
#     ],
#     AttributeDefinitions=[
#         {"AttributeName": "user_id", "AttributeType": "S"},
#     ],
#     BillingMode="PAY_PER_REQUEST"
# )
#
# print("✅ Table 'chopchop_goals' created.")
