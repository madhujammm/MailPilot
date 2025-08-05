import smtplib
from email.message import EmailMessage
import random
import time

# Your email credentials
SENDER_EMAIL = "madhujamm22@gmail.com" 
APP_PASSWORD = "minbfoednugqwkqw"     # not your real password

# Receiver (you can send to yourself)
RECEIVER_EMAIL = SENDER_EMAIL

# Fake email templates
fake_emails = [
    {
        "subject": "Important Update: Semester Registration Opens Tomorrow",
        "body": "Dear Student,\n\nThis is a reminder that registration for the upcoming semester starts tomorrow at 10 AM. Please login to the portal to choose your courses.\n\nAcademic Office"
    },
    {
        "subject": "🎓 Your Exam Schedule is Live Now",
        "body": "Hey, your final exam timetable has been published. Please check the college ERP system and be prepared accordingly.\n\nBest,\nCollege Admin"
    },
    {
        "subject": "🎉 You've WON a ₹10,000 Gift Card! Click to Claim!",
        "body": "Congratulations! You’ve been selected for a ₹10,000 Flipkart gift card. Click here to claim your prize: [FAKE LINK]\nOffer expires soon!"
    },
    {
        "subject": "Limited Offer: Earn ₹5000/day working from home",
        "body": "No experience needed! Join our part-time remote work team and start earning today. Sign up here: [SPAM LINK]"
    },
    {
        "subject": "College Fest Volunteer Registration Open",
        "body": "Hey students! Want to join the organizing committee for our annual tech fest? Fill this form to register before Aug 10.\n\nCheers,\nStudent Council"
    },
    {
        "subject": "⚠️ Your ATM card is suspended. Reactivate immediately.",
        "body": "We’ve noticed suspicious activity on your card. Click the link to verify your account and avoid suspension.\n[Fake Bank URL]"
    }
]

# Send emails
def send_email(subject, body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
        print(f"✅ Sent: {subject}")

# Send 10 random emails
for _ in range(10):
    email = random.choice(fake_emails)
    send_email(email["subject"], email["body"])
    time.sleep(1)  # slight delay to avoid getting flagged

print("🚀 All fake emails sent!")
