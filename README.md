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
```plaintext
game-day-notifications/
├── src/
│   ├── lambda_function.py      # Main Lambda function code
├── policies/
│   ├── sns_publish_policy.json # SNS publishing permissions
│   ├── eventbridge_invoke_policy.json # EventBridge to Lambda permissions
│   └── lambda_execution_policy.json # Lambda execution role permissions
├── .env                        # Environment variables for sensitive keys
├── .gitignore
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/YourGitHubUsername/nba-game-alerts.git
cd nba-game-alerts

