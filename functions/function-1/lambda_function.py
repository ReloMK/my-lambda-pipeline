import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from Function 1!",
            "function": "function-1"
        })
    }
