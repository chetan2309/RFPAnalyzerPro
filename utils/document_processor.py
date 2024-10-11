import PyPDF2
from io import BytesIO
from utils.azure_openai import generate_summary, extract_dates
from dateparser import parse

def process_rfp(file):
    # Read PDF content
    pdf_reader = PyPDF2.PdfReader(BytesIO(file.read()))
    text_content = ""
    for page in pdf_reader.pages:
        text_content += page.extract_text()

    # Generate summary using Azure OpenAI
    summary = generate_summary(text_content)

    # Extract dates using Azure OpenAI
    dates = extract_dates(text_content)
    
    # Parse the most relevant date as the submission deadline
    submission_deadline = parse_submission_deadline(dates)

    # Extract title (assuming it's on the first page)
    title = pdf_reader.pages[0].extract_text().split('\n')[0]

    return {
        "title": title,
        "summary": summary,
        "submission_deadline": submission_deadline
    }

def parse_submission_deadline(dates_text):
    dates = dates_text.split('\n')
    for date_str in dates:
        date = parse(date_str, settings={'STRICT_PARSING': True})
        if date:
            return date
    return None
