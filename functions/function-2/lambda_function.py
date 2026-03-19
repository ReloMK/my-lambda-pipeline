import json
from datetime import datetime

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "Hello from Function 2 - updated!",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    }
