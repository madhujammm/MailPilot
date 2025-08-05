from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from send_email import send_summary  # ✅ import send_summary

# Load .env
load_dotenv()

# Init Groq LLM (LLaMA-3)
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama3-70b-8192",
)

# System prompt
messages = [
    SystemMessage(content="""
You're AgentIntern, a helpful and proactive AI Intern created to assist Madhu with productivity.
Greet her warmly, and then wait for her task request.
"""),
]

# First bot reply
response = llm.invoke(messages)
print("🧠 AgentIntern:", response.content)
messages.append(AIMessage(content=response.content))

# 🔁 Chat loop
while True:
    user_input = input("👩 Madhu: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("🧠 AgentIntern: Catch you later, Madhu! Keep crushing it! 💪")
        break

    # 🚫 Skip AI reply if it's an email summary request
    if "send" in user_input.lower() and "email" in user_input.lower():
        from gmail_reader import get_unread_email_summary
        summary = get_unread_email_summary()
        send_summary(summary)

        print("🧠 AgentIntern:", summary)  # Show in chat
        messages.append(HumanMessage(content=user_input))
        messages.append(AIMessage(content=summary))  # add real summary
        continue  # ✅ Skip the rest of loop, don’t call LLM

    # 🧠 Normal Chat Flow
    messages.append(HumanMessage(content=user_input))
    response = llm.invoke(messages)
    print("🧠 AgentIntern:", response.content)
    messages.append(AIMessage(content=response.content))
