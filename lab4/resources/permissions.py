'''
	You must replace c11284a125438l662056t1w263075376620-s3bucket-1iw34utmqbfxm with your bucket name
'''
import boto3
import json

S3API = boto3.client("s3", region_name="us-west-2") 
bucket_name = "c11284a125438l662056t1w263075376620-s3bucket-1iw34utmqbfxm"

policy_file = open("/home/ec2-user/environment/resources/public_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("Setting Permissions - DONE")