from PIL import Image, ImageFilter, ImageDraw
import json


def lambda_handler(event, context):
    im = Image.open('default.png')

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "pixel": im.getpixel((256, 256))
        }),
    }
