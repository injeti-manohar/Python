import boto3

connection = boto3.client('elbv2','eu-central-1')

response = connection.describe_target_groups(
    TargetGroupArns=[
        'arn:aws:elasticloadbalancing:eu-central-1:388376138984:targetgroup/GPTargetGrp/406007a43eebe42a',
    ],
)

print(response)