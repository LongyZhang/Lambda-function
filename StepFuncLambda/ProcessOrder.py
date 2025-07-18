import json

def lambda_handler(event, context):
    # TODO implement
    print(f"Processing Order: {json.dumps(event)}")
    return {
        "statusCode": 200,
        "status": "Order lambda has processed this order successfully"
    }