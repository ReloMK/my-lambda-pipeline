import json
from lambda_function import lambda_handler

def test_handler():
    response = lambda_handler({}, {})
    body = json.loads(response["body"])
    assert response["statusCode"] == 200
    assert body["message"] == "Hello from my CI/CD pipeline!"
    print("✅ Test passed!")

test_handler()
