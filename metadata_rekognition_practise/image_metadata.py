import json
import boto3


def lambda_handler(event, context):
    client = boto3.client("rekognition")
    s3 = boto3.client("s3")

    fileObj = s3.get_object(Bucket = "mycr-images" , Key="test.jpeg")
    file_content = fileObj["Body"].read()

    response = client.detect_labels(Image= {"Bytes" : file_content}, MinConfidence = 70)

    print (response)





# https://www.youtube.com/watch?v=3r_ue7TQkCE
    # https://docs.aws.amazon.com/rekognition/latest/dg/images-s3.html