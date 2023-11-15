import boto3
import json

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    s3_object = s3_client.get_object(Bucket='crosario-resume', Key='visits.json')
    json_file = s3_object['Body'].read().decode('utf-8') 
    dict = json.loads(json_file)
    visitors = dict['visits']
    
    dict['visits'] += 1
    json_data = json.dumps(dict)
    s3_client.put_object(Bucket='crosario-resume', Key='visits.json', Body=json_data)

    return {
        'statusCode': 200,
        'body': json.dumps({'visits': visitors})
    }


