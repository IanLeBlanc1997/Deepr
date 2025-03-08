import requests
import os

def send_tweet(message):

    # API endpoint for creating tweets
    url = "https://api.twitter.com/2/tweets"
    
    # Set up your bearer token (from environment variable for security)
    bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")
    
    # Set up headers with authorization
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": message
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    # Error handling
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None
