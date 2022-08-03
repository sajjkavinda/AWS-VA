import json
import boto3
region ="us-east-1"

def lambda_handler(event, context):

    ec2 = boto3.client('ec2')
    response = ec2.describe_security_groups(
    Filters=[
        {
            'Name': 'ip-permission.cidr',
            'Values': [
                '0.0.0.0/0',
            ], 
            'Name': 'ip-permission.to-port',
            'Values': ['22']
        },
    ],
 )
    print(response)