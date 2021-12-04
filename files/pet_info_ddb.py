# Read json file on S3 bucket and write onto DDB 
import json
import boto3


def lambda_handler(event, context):
    
    
    s3_client = boto3.client('s3')

    
    bucket = 'mycr-json-files'
    key = 'pets_info.json'
    
    response = s3_client.get_object(Bucket = bucket, Key = key)
    content = response['Body']
    jsonObject = json.loads(content.read())
    # print(jsonObject)
    # return jsonObject

    
    # table.put_item(Item=jsonObject[0]['name'])
    # print(jsonObject[0]['name'])
    # print(jsonObject[1]['name'])
    # print(jsonObject[1]['species'])
    
        
    
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




# https://www.youtube.com/watch?v=-iYkKswrDbs