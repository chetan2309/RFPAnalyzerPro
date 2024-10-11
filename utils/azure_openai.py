import os
from openai import AzureOpenAI

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version="2023-05-15",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"]
)

deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]

def generate_summary(text):
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are an AI assistant that summarizes RFP documents."},
            {"role": "user", "content": f"Please provide a one-page executive summary of the following RFP document:\n\n{text}"}
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

def extract_dates(text):
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are an AI assistant that extracts important dates from RFP documents."},
            {"role": "user", "content": f"Please extract all important dates related to submission deadlines from the following RFP document. Return the dates in ISO format (YYYY-MM-DD):\n\n{text}"}
        ],
        max_tokens=100
    )
    return response.choices[0].message.content
