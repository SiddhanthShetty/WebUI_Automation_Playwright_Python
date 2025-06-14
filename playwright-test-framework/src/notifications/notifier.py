import os
from slack_sdk import WebClient

def send_slack_notification(message):
    slack_token = os.getenv("SLACK_TOKEN")
    channel = os.getenv("SLACK_CHANNEL")
    if slack_token and channel:
        client = WebClient(token=slack_token)
        client.chat_postMessage(channel=channel, text=message)

