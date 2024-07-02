
# AWS Lambda Function Documentation

## Sample Pure Lambda Function

This is a Python function that serves as a sample AWS Lambda function. It is designed to be used as part of an API Gateway Lambda Proxy integration, which allows the API Gateway to directly invoke the Lambda function and handle the response.

### Function Parameters

The `lambda_handler` function takes two parameters:

1. `event`: a dictionary that contains information about the incoming API request, such as the HTTP method, headers, and query parameters.
2. `context`: an object that provides information about the current execution context, such as the function name, version, and remaining execution time.

### Function Return Value

The function returns a dictionary in the API Gateway Lambda Proxy Output Format, with the following keys:

- `statusCode`: an HTTP status code (e.g., 200 for success, 400 for error)
- `body`: a JSON-encoded string containing the response data

The function currently returns a hardcoded "hello world" message in the response body.

### Example Usage

Here's an example of how the `lambda_handler` function can be used:

```python
import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world"
        }),
    }
```

For more information, please refer to the following documentation:

- [API Gateway Lambda Proxy Input Format](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format)
- [Lambda Context Object](https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html)
- [API Gateway Lambda Proxy Output Format](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html)
