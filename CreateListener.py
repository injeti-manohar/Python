import boto3

connection = boto3.client('elbv2','eu-central-1a')

response = connection.create_listener(
    DefaultActions=[
        {
            'TargetGroupArn': 'arn:aws:elasticloadbalancing:eu-central-1:388376138984:targetgroup/GPTargetGrp/406007a43eebe42a',
            'Type': 'forward',
        },
    ],
    LoadBalancerArn='arn:aws:elasticloadbalancing:eu-central-1:388376138984:loadbalancer/net/GPTestLoadBalancer/5aa0bff8c2b33081',
    Port=80,
    Protocol='HTTP',
)

print(response)