import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    bucket = "prarthan-jsonfiles"
    json_file_name = "emp.json"
    content_object = s3.Object(bucket,json_file_name)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    print(str(event))
    return json_content['Employees']
    


