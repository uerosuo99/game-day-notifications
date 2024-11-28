import boto3
import os
import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from datetime import datetime

# Initialize SNS client
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    # Get today's date in the required format (yyyy-MM-dd)
    today_date = datetime.now().strftime('%Y-%m-%d')
    
    # NBA API Config
    api_key = os.environ['NBA_API_KEY']
    api_url = f"https://api.sportsdata.io/v3/nba/scores/json/GamesByDateFinal/{today_date}?key={api_key}"

    try:
        # Make an HTTP GET request using urllib
        request = Request(api_url)
        response = urlopen(request)
        response_body = response.read().decode('utf-8')
        games = json.loads(response_body)

        # Check if there are no games
        if not games:
            no_games_message = "No relevant game updates now."
            sns_client.publish(
                TopicArn=os.environ['SNS_TOPIC_ARN'],
                Message=no_games_message,
                Subject="NBA Game Day Update"
            )
            return {
                "statusCode": 200,
                "body": no_games_message
            }

        # Format message for games
        messages = []
        for game in games:
            # Extract key game details
            status = game.get('Status')
            home_team = game.get('HomeTeam')
            away_team = game.get('AwayTeam')
            home_score = game.get('HomeTeamScore')
            away_score = game.get('AwayTeamScore')
            start_time = game.get('DateTime')
            channel = game.get('Channel')
            last_play = game.get('LastPlay', "No data available")
            quarters = game.get('Quarters', [])

            # Handle scores: If null, replace with a placeholder
            home_score_text = home_score if home_score is not None else "Not available yet"
            away_score_text = away_score if away_score is not None else "Not available yet"

            if status == "Final":
                # For Final games, include full details and quarter scores
                quarter_scores = []
                for quarter in quarters:
                    quarter_scores.append(f"Q{quarter['Number']}: {quarter['AwayScore']}-{quarter['HomeScore']}")
                quarter_scores_text = ", ".join(quarter_scores) if quarter_scores else "No quarter scores available"

                message = (
                    f"Game Status: {status}\n"
                    f"{away_team} vs {home_team}\n"
                    f"Final Score: {away_score}-{home_score}\n"
                    f"Start Time: {start_time}\n"
                    f"Channel: {channel}\n"
                    f"Quarter Scores: {quarter_scores_text}\n"
                )
                messages.append(message)

            elif status == "InProgress":
                # For InProgress games, include live updates
                message = (
                    f"Game Status: {status}\n"
                    f"{away_team} vs {home_team}\n"
                    f"Current Score: {away_score_text}-{home_score_text}\n"
                    f"Last Play: {last_play}\n"
                    f"Channel: {channel}\n"
                )
                messages.append(message)

        # Combine all messages
        final_message = "\n---\n".join(messages)

        # Publish to SNS Topic
        sns_client.publish(
            TopicArn=os.environ['SNS_TOPIC_ARN'],
            Message=final_message,
            Subject="NBA Game Day Update"
        )
        return {
            "statusCode": 200,
            "body": "Notifications sent successfully!"
        }

    except HTTPError as e:
        # Handle HTTP errors
        print(f"HTTPError: {e.code} - {e.reason}")
        return {
            "statusCode": e.code,
            "body": f"HTTPError: {e.reason}"
        }

    except URLError as e:
        # Handle URL errors
        print(f"URLError: {e.reason}")
        return {
            "statusCode": 500,
            "body": f"URLError: {e.reason}"
        }

    except Exception as e:
        # Handle any other exceptions
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
