from gmail_reader import fetch_emails_for_labeling
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# 🧠 Setup LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-70b-8192",
)

# 🛠️ Setup Gmail API
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os.path

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

def get_gmail_service():
    creds = None

    # Load token if it exists
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If no (valid) token available, start OAuth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the token for next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # Build and return Gmail API service
    from googleapiclient.discovery import build
    service = build("gmail", "v1", credentials=creds)
    return service

# 📌 Categorize with GPT
def categorize_email(subject, sender, snippet):
    prompt = f"""
Categorize this email into one of the following: [Internship, College, Bills, Spam, Other]

Subject: {subject}
From: {sender}
Snippet: {snippet}

Only respond with the category name.
"""
    response = llm.invoke(prompt)
    return response.content.strip()

# 🏷️ Gmail API Helpers
def get_or_create_label(service, label_name):
    labels = service.users().labels().list(userId='me').execute().get('labels', [])
    for label in labels:
        if label['name'].lower() == label_name.lower():
            return label['id']

    new_label = {
        'name': label_name,
        'labelListVisibility': 'labelShow',
        'messageListVisibility': 'show'
    }
    created = service.users().labels().create(userId='me', body=new_label).execute()
    return created['id']

def apply_label(service, message_id, label_id):
    service.users().messages().modify(
        userId='me',
        id=message_id,
        body={'addLabelIds': [label_id]}
    ).execute()

# 🚀 Run Auto-Labeler
def run_auto_labeler():
    service = get_gmail_service()
    emails = fetch_emails_for_labeling()
    print(f"📩 Emails fetched: {len(emails)}")  # Debug print

    if not emails:
        print("😴 No unread emails to label.")
        return

    for email in emails:
        print(f"🔍 Processing: {email['subject']} from {email['sender']}")  # Debug print
        category = categorize_email(email['subject'], email['sender'], email['snippet'])
        label_id = get_or_create_label(service, category)
        apply_label(service, email['id'], label_id)
        print(f"✅ Labeled: '{email['subject']}' ➡️ {category}")

if __name__ == "__main__":
    run_auto_labeler()
        

