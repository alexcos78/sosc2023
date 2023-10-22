#!/usr/bin/env python3

import boto3
import json

s3client = boto3.client('s3',
    aws_access_key_id = 'sosc1',
    aws_secret_access_key = 'sosc20231',
    endpoint_url="https://vm-131-154-99-202.cloud.cnaf.infn.it:9000",
    region_name='default',)


#List buckets
#resp = s3client.list_buckets()
#print(resp)


#Create bucket
#bucket_name = 'bucket1'
#s3bucket = s3client.create_bucket(Bucket=bucket_name)
#resp = s3client.list_buckets()
#print(resp)


#Print only bucket name
#resp = s3client.list_buckets()
#for bucket in resp['Buckets']:
#        print(bucket['Name'])



# Retrieve the policy of the specified bucket
#bucket_name = 'bucket1'
#resp = s3client.get_bucket_policy(Bucket=bucket_name,)
#print(resp)
#print(resp['Policy'])



# Create a bucket policy
#bucket_name = 'bucket1'
#bucket_policy = {
#    'Version': '2012-10-17',
#    'Statement': [{
#        'Sid': 'AddPerm',
#        'Effect': 'Allow',
#        'Principal': '*',
#        'Action': ['s3:ListBucket'],
#        'Resource': f'arn:aws:s3:::{bucket_name}'
#    }]
#}

# Convert the policy from JSON dict to string
#bucket_policy = json.dumps(bucket_policy)

# Set the new policy
#s3client.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
#resp = s3client.get_bucket_policy(Bucket='bucket1',)
#print(resp)



#Upload object
#bucket_name = 'bucket1'
#upload = s3client.upload_file('test2.txt', bucket_name, 'test/test2.txt')
#resp = s3client.list_objects(Bucket=bucket_name)
#print(resp)



#List object
#bucket_name = 'bucket1'
#resp = s3client.list_objects(Bucket=bucket_name)
#print(resp)
#for object in resp['Contents']:
#        print(object['Key'])



#List metadata
#bucket_name = 'bucket1'
#resp = s3client.list_objects(Bucket=bucket_name)
##print(resp)
#for object in resp['Contents']:
#    print(object['Key'])
#    metadata = s3client.head_object(Bucket=bucket_name, Key=object['Key'])
#    print(metadata)



#Add metadata
#bucket_name = 'bucket1'
#resp = s3client.list_objects(Bucket=bucket_name)
##print(resp)
#for object in resp['Contents']:
#    print(object['Key'])
#    metadata = s3client.head_object(Bucket=bucket_name, Key=object['Key'])
#    print(metadata)
#    new_meta = metadata['Metadata']
#    new_meta['Costa'] = 'costa'
#    s3client.copy_object(Bucket=bucket_name, Key=object['Key'], CopySource=bucket_name + '/' + object['Key'], Metadata=new_meta, MetadataDirective='REPLACE')



#Remove object
#bucket_name = 'bucket1'
#resp = s3client.list_objects(Bucket=bucket_name)
#print(resp)
#for object in resp['Contents']:
#    print(object['Key'])
#    s3client.delete_object(Bucket=bucket_name, Key=object['Key'])
#resp = s3client.list_objects(Bucket=bucket_name)
#print(resp)
