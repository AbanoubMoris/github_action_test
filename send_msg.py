import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


client = WebClient(token='xoxb-426373988017-4558141128291-9Xhz5FvUtBvCMy9O5yFZJvpt')

def notify_slack(message):
    try:
        response = client.chat_postMessage(channel='qa-testing_bot', text=message)
        print(response["message"]["text"])
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")