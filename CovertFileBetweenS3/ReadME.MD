# 📄 AWS Lambda CSV to JSON Converter

This project demonstrates how to use an **AWS Lambda** function to automatically convert `.csv` files to `.json`. The function is triggered when a CSV file is uploaded to a source S3 bucket. The output is saved in a destination S3 bucket.

---

## 🧠 Logic Overview

1. A user or API uploads a `.csv` file to the **source S3 bucket**.
2. The **S3 event** triggers a **Lambda function**.
3. The Lambda function:
   - Downloads the CSV file
   - Converts it to JSON format
   - Uploads the result to the **destination S3 bucket**

---

## 🛠️ Setup Instructions

### ✅ Step 1: Create Two S3 Buckets

- Source bucket: `source-bucket-lgzhang`
- Destination bucket: `destination-bucket-lgzhang`

> You can name the buckets anything you like, but make sure they match in the Lambda environment variables and permissions.

---

### ✅ Step 2: Create Lambda Function (Python)

1. Runtime: **Python 3.10**
2. Function name: `csvToJsonConverter` (or any name you prefer)
3. Add the following **environment variable**:

4. Paste the Lambda code (see below) into the function editor



### ✅ Step 3: Attach IAM Permissions to Lambda
Attach the following inline policy to the Lambda execution role:


{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "S3AccessForLambda",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "*"
    }
  ]
}


### ✅ Step 4: Configure S3 Event Notification
Go to the source bucket

Navigate to: Properties → Event notifications → Create event notification

Name: trigger-lambda-on-csv-upload

Event type: PUT

Optional suffix: .csv

Destination: Lambda function (csvToJsonConverter)

🧠 Author
Maintained by Longhan Zhang
📅 Last updated: July 16, 2025

