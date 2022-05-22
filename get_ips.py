import boto3

client = boto3.client('ec2')

custom_filter = [{
    'Name':'tag:Environment', 
    'Values': ['DEV']}]
    
response = client.describe_instances(Filters=custom_filter)
