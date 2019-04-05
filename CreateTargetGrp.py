

import boto3

connection = boto3.client('elbv2', 'eu-central-1')

response = connection.create_target_group(
    Name='GPTargetGrp',
    Protocol='TCP',
    Port=80,
    VpcId='vpc-03a9c81b99ce19b06',
)

print(response)