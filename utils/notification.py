import os
import requests
from config import Config

def send_teams_notification(message):
    payload = {
        "text": message
    }
    try:
        response = requests.post(Config.TEAMS_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        print(f"Notification sent successfully: {message}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send notification: {e}")
