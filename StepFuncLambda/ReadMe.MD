# 📦 Order Processing Workflow (AWS Step Functions)

This Step Functions workflow automates the processing of online orders. It includes conditional logic for applying discounts, sending the order to an SQS queue, processing the order via Lambda, and notifying via SNS email.

---

## 📐 Architecture Diagram

![Architecture Diagram](https://github.com/LongyZhang/Lambda-function/blob/0b0ac3cd8b02254ec9dede481561d7bed10cd89e/step_func.png)

---

## 🧩 Components Used

- **Step Functions**: Orchestration of the entire workflow
- **Lambda Functions**:
  - `ApplyDiscount`: Applies a discount if `couponCode` is valid
  - `ProcessOrder`: Finalizes the order after queueing
- **SQS Queue**: Used to asynchronously queue the order
- **SNS Topic**: Sends an email notification once the order is processed

---

## 🔁 Workflow Logic

```text
             ┌────────────────────┐
             │ CheckCouponCode    │
             └────────┬───────────┘
        has coupon?  / \ no
                    /   \
      ┌─────────────┐   ┌────────────┐
      │ApplyDiscount│   │Add "NoCoupon" Info│
      └────┬────────┘   └────────────┘
           ↓
     ┌────────────────────┐
     │ Send to SQS Queue  │
     └────────┬───────────┘
              ↓
     ┌─────────────────────────────┐
     │       Parallel Execution    │
     ├────────────┬───────────────┤
     │  ProcessOrder Lambda       │
     │  Send SNS Email Notification │
     └─────────────────────────────┘

📥 Sample Input

{
  "orderId": "A1001",
  "customerEmail": "customer@example.com",
  "items": [
    "apple",
    "banana"
  ],
  "couponCode": "DISCOUNT20",
  "price": 90
}


📥 Sample Output in email 
New order received: Order ID 63a15c97-b839-4c23-9fdd-a70b4cecfea7 for ["apple","banana"] items at a price of 72.0

