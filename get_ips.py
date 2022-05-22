import boto3
from pprint import pprint

client = boto3.client('ec2', region_name="ap-south-1")

custom_filter = [{
    'Name':'tag:Environment',
    'Values': ['TEST']}
]

response = client.describe_instances(Filters=custom_filter)
for instance in response["Reservations"]:
    for _ins in instance["Instances"]:
        pprint(_ins["PrivateIpAddress"])
