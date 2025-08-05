from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

creds = Credentials.from_authorized_user_file('token.json')
service = build('gmail', 'v1', credentials=creds)

results = service.users().labels().list(userId='me').execute()
labels = results.get('labels', [])

print('Labels:')
for label in labels:
    print(f"- {label['name']}")
