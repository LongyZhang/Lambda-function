import json 
import logging

## error handler

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    logger.info(f"Event received => {json.dumps(event)}")

    # Log Context object
    logger.info(f"Context received => {context}")
    logger.info('Hello from Longy')

    ## receive the input from event.

    ## If the couponCode is matched, we change the value of event (input) by discount.

    ## else they will be invalid code.

    try:
        if "couponCode" in event:
            if event["couponCode"] == "DISCOUNT10":
                event["price"] = round(event["price"] * 0.9,2)
            elif event["couponCode"] == "DISCOUNT20":
                event["price"] = round(event["price"] * 0.8, 2)
            elif event["couponCode"] == "DISCOUNT30":
                event["price"] = round(event["price"] * 0.7, 2)
            else:
                event["update"] = "Invalid code"
        return event
    except Exception as e:
        logger.error(f"Error info => {e}")
        return {"statusCode": 500, "body": json.dumps({"message": "Internal Server Error"})}