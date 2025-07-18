# 🧠 AWS Lambda Learning & Practice Log

This repository documents my journey learning and practicing **AWS Lambda** functions using Python (or Node.js, etc.). It includes code samples, deployment scripts, test cases, and notes on integrating Lambda with other AWS services.

---

## 📌 Learning Goals

- Understand Lambda execution model and lifecycle
- Write, test, and deploy Lambda functions using the AWS Console, AWS CLI, and Terraform/CDK
- Learn to work with common event triggers (S3, API Gateway, CloudWatch, EventBridge)
- Explore asynchronous invocation, retries, DLQs, and logging
- Practice best practices: cold start mitigation, environment variables, IAM permissions, and packaging
- Build real-world use cases (e.g., image processing, log parsing, REST APIs)

---


## 🛠️ Practice Logs

| Date       | Topic/Exercise                         | Notes/Outcome                                               |
|------------|-----------------------------------------|-------------------------------------------------------------|
| 2025-07-16 | Created hello world Lambda (Python)     | Used AWS Console to test inline; logged output to CloudWatch |
| 2025-07-17 | S3 trigger with Lambda                  | Lambda triggered on file upload; Convert file from CSV to Json |
| 2025-07-18 | Step function, SQS, SNS and Lambda      | Built simple Order system by using severless step function        |




## ✅ To-Do

- [ ] Add more event sources (e.g., DynamoDB, EventBridge)
- [ ] Build a scheduled job using CloudWatch
- [ ] Explore Lambda Layers
- [ ] Integrate with SNS/SQS
- [ ] Add CI/CD workflow for deployments

---

> Last updated: 2025-07-16

