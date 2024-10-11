import os

class Config:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEAMS_WEBHOOK_URL = "https://tavant.webhook.office.com/webhookb2/0046ec07-e104-4c37-8c93-82ff16312f00@c6c1e9da-5d0c-4f8f-9a02-3c67206efbd6/IncomingWebhook/a20d9ad0021a4644bbf129d53bbf0548/44d37ec7-fae7-4a3b-9f41-b8f3539805da/V2Fs8urqLM56bQ80EZsNlWjLnz0400WBsSrhu_ktXCOC41"
