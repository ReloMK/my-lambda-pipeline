import json

def lambda_handler(event, context):
    number1 = 10
    number2 = 20
    result = number1 + number2
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from Function 3!",
            "calculation": f"{number1} + {number2} = {result}"
        })
    }
