import json
import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']
    
    
    json_object = s3_client.get_object(Bucket=bucket,Key=json_file_name)
    jsonFileReader = json_object['Body'].read()
    jsonObject = json.loads(jsonFileReader)
    # table = dynamodb.Table('pets')
    # table.put_item(Item=jsonDict)
    
    # print(bucket)
    # print(json_file_name)
    # print(str(event))
    
    dynao_list = []
    i =0
    while i < len(jsonObject):
        for items in jsonObject:
            
            main_dic = {}
            main_dic['name'] = jsonObject[i]['name']
            main_dic['species'] = jsonObject[i]['species']
            main_dic['FevFood'] = jsonObject[i]['favFoods']
            main_dic['BirthYear'] = jsonObject[i]['birthYear']
            main_dic['Photo'] = jsonObject[i]['photo']
            dynao_list.append(main_dic)
            i += 1
            
        print(dynao_list)
        
        
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('pets')
        for i in range(0,len(dynao_list)):
            table.put_item(Item=dynao_list[i])



 # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
    
# # https://www.youtube.com/watch?v=-iYkKswrDbs




