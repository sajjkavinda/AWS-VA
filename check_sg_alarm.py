import boto3
from botocore.vendored import requests
import json
client1 = boto3.client('ec2')
def lambda_handler(event, context):
    
    security_groupId = event['detail']['requestParameters']['groupId']
    cidr_string = str(event['detail']['requestParameters']['ipPermissions'])
    if '0.0.0.0/0' in cidr_string:
        
        response = client1.describe_security_groups(Filters=[
            {
                'Name': 'group-id',
                'Values': [
                    security_groupId,
                ]
            },
        ])
        print(response)
        SecurityGroupName = response['SecurityGroups'][0]['GroupName']
        OwnerId = response['SecurityGroups'][0]['OwnerId']
        VPC_Id = response['SecurityGroups'][0]['VpcId']
        
        message = "Open Security Group Found in AWS:\n"+"Security GroupName: "+SecurityGroupName+"\nSecurity GroupId: "+security_groupId+"\nVPC Id: "+VPC_Id+"\nOwner Id: "+OwnerId
        
        response = client1.describe_network_interfaces(Filters=[
            {
                'Name': 'group-id',
                'Values': [
                    security_groupId,
                ]
            },
        ])
        print(response)
        if (len(response['NetworkInterfaces']) > 0):
            if 'InstanceId' in response['NetworkInterfaces'][0]['Attachment'].keys():
                print("InstanceId is:", response['NetworkInterfaces'][0]['Attachment']['InstanceId'])
                InstanceId = response['NetworkInterfaces'][0]['Attachment']['InstanceId']
                message = message+"\nInstance Id (using this Security Group): "+InstanceId
                    
            else:
                print("Resource associated:", response['NetworkInterfaces'][0]['Attachment']['InstanceOwnerId'])
                print("Resource description:", response['NetworkInterfaces'][0]['Description'])
                ResourceAssociated = response['NetworkInterfaces'][0]['Attachment']['InstanceOwnerId']
                ResourceDescription = response['NetworkInterfaces'][0]['Description']
                message = message+"\nResource Associated: "+ResourceAssociated+"\nResource Description: "+ResourceDescription
                    
        else:
            print("This Security Group is Not associated with any resource yet!")
            message = message+"\nThis Security Group is not associated with any resource yet!"
            
        webhook_url = 'https://hooks.slack.com/services/<slack-webhook-url>/<webhook token>'
        slack_message = {'text':message}
        requests.post(webhook_url,data=json.dumps(slack_message))
    
    else:
        print("Everything seems to be fine!")