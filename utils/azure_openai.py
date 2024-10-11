import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Initialize the Azure Text Analytics client
endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
key = os.environ["AZURE_OPENAI_API_KEY"]

text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

def generate_summary(text):
    try:
        response = text_analytics_client.extractive_summarization(documents=[text])[0]
        return " ".join([sentence.text for sentence in response.sentences])
    except Exception as e:
        print(f"Error generating summary: {str(e)}")
        return "Unable to generate summary."

def extract_dates(text):
    try:
        response = text_analytics_client.recognize_entities(documents=[text])[0]
        dates = [entity.text for entity in response.entities if entity.category == "DateTime"]
        return "\n".join(dates)
    except Exception as e:
        print(f"Error extracting dates: {str(e)}")
        return "Unable to extract dates."
