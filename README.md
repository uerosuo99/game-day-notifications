# NBA Game Day Notifications / Sports Alerts System

## **Project Overview**
This project is an alert system that sends real-time NBA game day score notifications to subscribed users via SMS/Email. It leverages **Amazon SNS**, **AWS Lambda and Python**, **Amazon EvenBridge** and **NBA APIs** to provide sports fans with up-to-date game information. The project demonstrates cloud computing principles and efficient notification mechanisms.

---

## **Features**
- Fetches live NBA game scores using an external API.
- Sends formatted score updates to subscribers via SMS/Email using Amazon SNS.
- Scheduled automation for regular updates using Amazon EventBridge.
- Designed with security in mind, following the principle of least privilege for IAM roles.

---

## **Technical Architecture**
- **Cloud Provider**: AWS
- **Core Services**: SNS, Lambda, EventBridge
- **External API**: NBA Game API (e.g., SportsData.io, BallDontLie, or RapidAPI)
- **Programming Language**: Python 3.x
- **Dependencies**:
  - `boto3`: AWS SDK for Python
  - `requests`: HTTP requests for NBA API
- **IAM Security**:
  - Least privilege policies for Lambda, SNS, and EventBridge.

---

## **Project Structure**
```bash
game-day-notifications/
├── src/
│   ├── lambda_function.py               # Main Lambda function code
├── policies/
│   ├── sns_publish_policy.json          # SNS publishing permissions
│   ├── eventbridge_invoke_policy.json   # EventBridge to Lambda permissions
│   └── lambda_execution_policy.json     # Lambda execution role permissions
├── .gitignore
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation
```

## **Setup Instructions**

### **Clone the Repository**
```bash
git clone https://github.com/YourGitHubUsername/nba-game-alerts.git
cd nba-game-alerts
```

### **Install Dependencies**
```bash
pip install -r requirements.txt
```


### **Create an SNS Topic**
1. Open the AWS Management Console.
2. Navigate to the SNS service.
3. Click Create Topic and select Standard as the topic type.
4. Name the topic (e.g., NBA_Game_Alerts) and note the ARN.
5. Click Create Topic.


### **reate an IAM Role for Lambda**
1. Open the IAM service in the AWS Management Console.
2. Click Roles → Create Role.
3. Select AWS Service and choose Lambda.
4. Attach the following policies:
  - SNS Publish Policy (sns_publish_policy.json)
  - EventBridge Invoke Policy (eventbridge_invoke_policy.json)
  - Lambda Execution Policy (lambda_execution_policy.json)SNS Publish Policy, EventBridge Invoke Policy, Lambda Execution Policy
5. Name the role (e.g., NBA_Lambda_Role) and create it.
6. Copy and Save the ARN of the role.


### **Deploy the Lambda Function**
Zip the Lambda code:
```bash
zip -r function.zip src/
```


### **Set Up Automation with Eventbridge**
Navigate to EventBridge → Rules → Create Rule.
Choose Event Source: Schedule.
Set the cron schedule for when you want updates (e.g., hourly).
Add the Lambda function as the target and save the rule.


### **Test the System**
Use test events in the Lambda console to simulate execution.
Check the SNS subscriptions to verify SMS/Email notifications.
Debug any errors using CloudWatch Logs.


### **What I Learned**
Designing a notification system with AWS SNS and Lambda.
Securing AWS services with least privilege IAM policies.
Automating workflows using EventBridge.
Integrating external APIs into cloud-based workflows.


### **Future Enhancements**
Add NFL score alerts for extended functionality.
Store user preferences (teams, game types) in DynamoDB for personalized alerts.
Implement a web UI
