# 📄 CSV to JSON Converter with AWS Lambda

This project demonstrates how to automatically convert a CSV file to JSON format using an AWS Lambda function, triggered by an S3 event.

---

## 🧠 Logic Overview

1. A **user or API** uploads a CSV file to the **source S3 bucket**.
2. The **S3 event** triggers a **Lambda function**.
3. The **Lambda function** reads the CSV, converts it to JSON.
4. The function writes the resulting JSON file to a **destination S3 bucket**.

---

## 🛠️ Step-by-Step Setup

### ✅ Step 1: Create S3 Buckets

- Create a **source bucket** (e.g., `source-bucket-lgzhang`)
- Create a **destination bucket** (e.g., `destination-bucket-lgzhang`)

---

### ✅ Step 2: Create the Lambda Function

- Language: **Python**
- Attach the following **environment variable** to your Lambda:

```env
DESTINATION_BUCKET = destination-bucket-lgzhang
