import smtplib
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(news_list, recipient_email):
    """Sends an email with the latest news articles."""
    sender_email = st.secrets["general"]["EMAIL"]
    app_password = st.secrets["general"]["APP_PASSWORD"]
    
    subject = "Your Daily Newsletter"
    body = "\n\n".join([f"{news['title']}: {news['description']}\n{news['url']}" for news in news_list])
    
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
