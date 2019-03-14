import json
import boto3
import re


s3 = boto3.resource('s3')
api_client = s3.meta.client

def lambda_handler(event, context):
    bucket = "prarthan-jsonfiles"
    json_file_name = "emp.json"
    content_object = s3.Object(bucket,json_file_name)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    
    for key,value in json_content.items():
        for i in value:
            id=event['id']
            if i['id']==id:
                i['name']='Alex'
                dumping=json.dumps(json_content, ensure_ascii=False) # dictionary to json

                object = s3.Object(bucket,json_file_name )
                object.put(Body=dumping)
                client = boto3.client('s3')
                client.put_object(Body=dumping, Bucket=bucket, Key=json_file_name) # loading updated json to s3 bucket
                
    return json_content

    
    