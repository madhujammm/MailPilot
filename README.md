# 📬 MailPilot – AI-Powered Email Labeling Assistant

Automatically scans unread emails, understands their content using LLM (LLaMA3 via Groq), and labels them in your Gmail account using Gmail API.

---

## 🧠 Features

* 🔍 Fetch unread emails from Gmail
* 🤖 Auto-categorize using GPT (via Groq + LLaMA3)
* 🏷️ Auto-apply Gmail labels: `Internship`, `College`, `Bills`, `Spam`, `Other`
* ♻️ Creates labels if they don’t exist
* 🛡️ Secure OAuth2-based Gmail access
* 💬 Fully customizable LLM prompts

---

## 🚀 Demo (Coming soon)

Wanna see it in action? Video/GIF coming 🔜

---

## 🧰 Tech Stack

| Tool      | Purpose                                |
| --------- | -------------------------------------- |
| Python    | Core scripting language                |
| Gmail API | Fetch and label emails                 |
| OAuth2    | Secure Google account access           |
| Langchain | For LLM orchestration                  |
| Groq      | Runs LLaMA3-70B for categorization     |
| dotenv    | Manage secrets & environment variables |

---

## 🔧 Setup Instructions

### 1. 📁 Clone the Repo

```bash
git clone https://github.com/your-username/mailpilot.git
cd mailpilot
```

### 2. 🐍 Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
# or
source venv/bin/activate # On Mac/Linux
```

### 3. 📦 Install Requirements

```bash
pip install -r requirements.txt
```

### 4. 🔑 Setup `.env`

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. 🧾 Set Up Gmail OAuth

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project → Enable **Gmail API**.
3. Go to “Credentials” tab:

   * Create **OAuth Client ID**
   * Application type → **Desktop App**
   * Download `credentials.json` into the project root.

---

## ▶️ Run the App

First-time run will open a browser for Gmail OAuth:

```bash
python email_labeler.py
```

Output:

```
📩 Emails fetched: 5
🔍 Processing: Internship offer from ABC Corp
✅ Labeled: 'Internship offer from ABC Corp' ➡️ Internship
```

---

## 📁 Project Structure

```
MailPilot/
│
├── email_labeler.py         # Main script that does all the magic
├── gmail_reader.py          # Fetches unread email details
├── credentials.json         # Gmail API credentials (DO NOT SHARE)
├── token.json               # Generated after OAuth
├── .env                     # Your secret Groq API key
└── requirements.txt         # Python dependencies
```

---

## 🧠 How Categorization Works

> Behind the scenes, your emails are summarized and passed to LLaMA3 (via Groq) with a prompt like:

```
Categorize this email into one of the following: [Internship, College, Bills, Spam, Other]
Subject: ...
From: ...
Snippet: ...
```

LLM returns the label name → Gmail API applies it → ✅ done!

---

## 🚨 Notes

* You must enable “Gmail API” in your Google Cloud project.
* Gmail tokens are stored in `token.json`. Delete it if OAuth bugs out.
* LLM behavior can vary; feel free to fine-tune the prompt or model.

---

## 🔮 Coming Soon

* 📥 Auto-archive emails by category
* 🔁 Periodic background scheduler
* 📊 Daily/weekly email insights dashboard
* 📨 Auto-responder for labeled emails


---

## 🛡️ License

MIT License

---

## 🧑‍💻 Author

Built with love (and lots of debug logs) by [Madhu](https://github.com/your-github).

---
