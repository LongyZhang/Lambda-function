## this ReadME file is about to introduce how i convert the file from CSV to Json.

## Logic: 
1: User or API upload the CSV file to S3

2: Source S3 bucket will notify the Lambda function

3: Lambda function change the file type to JSON

4: Put the file to Destination S3 bucket.

## Step 1: 
Create source and Destination bucket in S3

## Step 2： 
Create Lambad function by using python code.

In the Lambad function Environment Variables : 

Add the Key DESTINATION_BUCKET = destination-bucket-lgzhang

change the IAM rule for Lambda 
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": "*"
        }
    ]
}

## Step 2: 
GO to S3 bucket setting-> Property -> Event notification -> Add new rule, trigger Lambda function.

## Step 3:
test, add the CSV file to Source bucket, you should see copy of file in destination bucket.
