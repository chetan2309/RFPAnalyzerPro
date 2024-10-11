import os
from openai import AzureOpenAI

AZURE_OPENAI_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT_NAME = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")

# Initialize Azure OpenAI client
client = AzureOpenAI(api_key=AZURE_OPENAI_API_KEY,
                     api_version="2023-05-15",
                     azure_endpoint=AZURE_OPENAI_ENDPOINT)


def generate_summary(text):
    prompt = f"""Please provide a one-page executive summary of the following RFP document:
    Given the context information and not prior knowledge, provide a well-reasoned and informative response to the query. Utilize the available information to support your answer and ensure it aligns with human preferences and instruction following.
    {text}
    """
    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT_NAME,
        messages=[{
            "role": "user",
            "content": prompt
        }, {
            "role":
            "assistant",
            "content":
            "Here is the summary of the RFP document: <summary>"
        }],
        max_tokens=2000)
    return response.choices[0].message.content


def extract_dates(text):
    prompt = f"Please extract all important dates related to submission deadlines from the following RFP document. Return the dates in ISO format (YYYY-MM-DD):\n\n{text}"
    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT_NAME,
        messages=[{
            "role": "user",
            "content": prompt
        }],
        max_tokens=100)
    return response.choices[0].message.content


def generate_rfp_response(summary):
    prompt = f"""Based on the following RFP summary, generate a comprehensive response addressing the key points and requirements:

    {summary}

    Your response should include:
    1. An introduction demonstrating understanding of the project
    2. A high-level approach to meeting the RFP requirements
    3. Key differentiators or unique value propositions
    4. Any clarifying questions or additional information needed

    Please provide a well-structured and professional response."""

    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT_NAME,
        messages=[{
            "role": "user",
            "content": prompt
        }],
        max_tokens=2000)
    return response.choices[0].message.content
