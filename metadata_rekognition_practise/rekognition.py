#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def lambda_handler(event, context):

    client=boto3.client('rekognition')

    s3 = boto3.client("s3")
    fileObj = s3.get_object(Bucket = "mycr-images" , Key="test.jpeg")
    file_content = fileObj["Body"].read()

    response = client.detect_labels(Image= {"Bytes" : file_content}, MaxLabels=10)
    

    # print('Detected labels for ' + photo) 
    # print()   
    for label in response['Labels']:
        print ("Label: " + label['Name'])
        print ("Confidence: " + str(label['Confidence']))
        print ("Instances:")
        for instance in label['Instances']:
            print ("  Bounding box")
            print ("    Top: " + str(instance['BoundingBox']['Top']))
            print ("    Left: " + str(instance['BoundingBox']['Left']))
            print ("    Width: " +  str(instance['BoundingBox']['Width']))
            print ("    Height: " +  str(instance['BoundingBox']['Height']))
            print ("  Confidence: " + str(instance['Confidence']))
            print()

        print ("Parents:")
        for parent in label['Parents']:
            print ("   " + parent['Name'])
        print ("----------")
        print ()
    return len(response['Labels'])


def main():
    photo=''
    bucket=''
    label_count=detect_labels(photo, bucket)
    print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    main()



# https://www.youtube.com/watch?v=3r_ue7TQkCE
    # https://docs.aws.amazon.com/rekognition/latest/dg/images-s3.html