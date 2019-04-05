import boto3

connection = boto3.client('elbv2','eu-central-1')

response = connection.describe_load_balancers(
)

print(response)