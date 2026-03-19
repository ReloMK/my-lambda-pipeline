import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
           "message": "Hello from my CI/CD pipeline - version 2!",
            "version": "2.0.0"
        })
    }
