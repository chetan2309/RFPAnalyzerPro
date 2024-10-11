import os
import requests

TEAMS_WEBHOOK_URL = os.environ.get("TEAMS_WEBHOOK_URL")

def send_teams_notification(message):
    payload = {
        "text": message
    }
    try:
        response = requests.post(TEAMS_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print(f"Notification sent successfully: {message}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send notification: {e}")
