from PIL import Image, ImageFilter, ImageDraw
import json
import boto3
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    im = Image.open('default.png')
    response = s3_client.get_object(Bucket=os.environ['S3_BUCKET_NAME'], Key=os.environ['OBJECT_KEY_NAME'])
    body = response['Body'].read()
    print(body)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "pixel": im.getpixel((256, 256))
        }),
    }
