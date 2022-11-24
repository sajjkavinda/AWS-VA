import boto3
from botocore.vendored import requests
import json
Client = boto3.resource('ec2')
client = boto3.client('ec2', region_name='us-east-1')
def lambda_handler(event, context):
    count = 0
    sgs=client.describe_security_groups()["SecurityGroups"]
    for sg in sgs:
       
        sg_details = Client.SecurityGroup(sg["GroupId"])
        if '0.0.0.0/0' in str(sg_details.ip_permissions):
            count=count+1
            print ("SecurityGroupId:", sg["GroupId"], "SecurityGroupName:", sg["GroupName"])
            response = client.describe_network_interfaces(Filters=[
                {
                    'Name': 'group-id',
                    'Values': [
                        sg["GroupId"],
                    ]
                },
            ])
            if (len(response['NetworkInterfaces']) > 0):
                if 'InstanceId' in response['NetworkInterfaces'][0]['Attachment'].keys():
                    print("InstanceId is:", response['NetworkInterfaces'][0]['Attachment']['InstanceId'])
                    print("***********************************")
                        
                else:
                    print("Resource associated:", response['NetworkInterfaces'][0]['Attachment']['InstanceOwnerId'], "Resource description:", response['NetworkInterfaces'][0]['Description'])
                    print("***********************************")
                    
            else:
                #print("This Security Group is Not associated with any resource yet!")
                print ("No information found for this Security Group!")
                print("***********************************")
                    
    print ("Total Vulnerabilities Found: ", count)