import json
import boto3
import csv
import io
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Set the desired logging level

s3 = boto3.client("s3")


def lambda_handler(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    # Log event to CloudWatch
    logger.info(f"Event received => {json.dumps(event)}")

    # Log Context object
    logger.info(f"Context received => {context}")

    try:
        # Get CSV file
        response = s3.get_object(Bucket=bucket, Key=key)
        csv_content = response["Body"].read().decode("utf-8")

        # Convert CSV to JSON
        reader = csv.DictReader(io.StringIO(csv_content))
        json_data = json.dumps([row for row in reader])

        # Get destination bucket from environment variable
        destination_bucket = os.environ.get("DESTINATION_BUCKET")

        # Save JSON to S3
        json_key = key.replace(".csv", ".json")
        s3.put_object(Bucket=destination_bucket, Key=json_key, Body=json_data)

        logger.info(f"Transformed {key} to {json_key}")

        return {
            "statusCode": 200,
            "body": json.dumps("CSV transformed to JSON and saved to S3!"),
        }
    except Exception as e:
        logger.error("Error during processing: %s", str(e))  # Log the error
        return {"statusCode": 500, "body": json.dumps({"message": "An error occurred"})}
