import boto3
import requests
import os

# Initialize SNS client
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    # NBA API Config
    api_url = "https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/2024-11-23"
    headers = {"Ocp-Apim-Subscription-Key": os.environ['NBA_API_KEY']}
    
    try:
        # Fetch game data
        response = requests.get(api_url, headers=headers)
        games = response.json()

        # Format message
        messages = []
        for game in games:
            messages.append(f"{game['HomeTeam']} vs {game['AwayTeam']} - {game['HomeTeamScore']}:{game['AwayTeamScore']}")

        final_message = "\n".join(messages)

        # Publish to SNS Topic
        sns_client.publish(
            TopicArn=os.environ['SNS_TOPIC_ARN'],
            Message=final_message,
            Subject="NBA Game Day Update!"
        )
        return {"statusCode": 200, "body": "Notifications sent successfully!"}
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
