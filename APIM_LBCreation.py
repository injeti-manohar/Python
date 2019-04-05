
import boto3

connection = boto3.client('elbv2', 'eu-central-1')

response = connection.create_load_balancer(
    Name='GPTestLoadBalancer',
    Subnets=[
        'subnet-08b206cd84b1fd48e',
    ],
    Scheme='internet-facing',
    Tags=[
        {
            'Key': 'LB',
            'Value': 'Testing'
        },
    ],
    Type='network',
    IpAddressType='ipv4'
)

print(response)