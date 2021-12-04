import json
import boto3

s3_client = boto3.client('s3')
# client = boto3.client('dynamodb')
client = boto3.resource('dynamodb')
# dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']
    
    
    json_object = s3_client.get_object(Bucket=bucket,Key=json_file_name)
    jsonFileReader = json_object['Body'].read()
    jsonDict = json.loads(jsonFileReader)
   
    # printing bucket details and json file name & event body    
    print(bucket)
    print(json_file_name)
    print(str(event))
    print(str(jsonDict))
    
    # assign dynamodb table name & put item 
    table = client.Table("pets")
    print(table.table_status)
    # table.put_item(Item= {'name': 'snake','age':  '5', 'food' : 'rat'})
    table.put_item(Item=jsonDict)
    
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


# aws lambda invoke --function-name read-s3-jason-lambda-test3 out.txt --log-type Tail