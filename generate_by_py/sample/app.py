from PIL import Image, ImageFilter, ImageDraw, ImageFont
import json
import boto3
import os
from io import BytesIO
import requests

s3_client = boto3.client('s3')
req = requests.get(os.environ['FONT_URL'], allow_redirects=True)

def lambda_handler(event, context):

    buffer = BytesIO()
    im = Image.new("RGB", (640, 480), (128, 128, 128))
    draw = ImageDraw.Draw(im)

    font1 = ImageFont.truetype(BytesIO(req.content), size=48)
    font2 = ImageFont.truetype(BytesIO(req.content), size=64)
    font3 = ImageFont.truetype(BytesIO(req.content), size=32)


    draw.text((100,50), "Hello World!!", font=font1, fill='white')
    draw.text((180, 180), "Foo Bar", font=font2, fill='black')
    draw.text((100, 300), "hogehoge", font=font3, fill='black')
    draw.text((400, 300), "MyApp", font=font1, fill='green')

    im.save(buffer, "PNG")
    buffer.seek(0)
    img_name = 'sample.png'
    s3_client.put_object(
        ACL=os.environ['S3_OBJECT_ACL'],
        Bucket=os.environ['S3_BUCKET_NAME'],
        Key=img_name,
        Body=buffer,
        ContentType='image/png',
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "pixel": im.getpixel((256, 256))
        }),
    }
