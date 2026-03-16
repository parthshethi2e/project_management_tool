import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(to_email, subject, html_body):

    msg = MIMEMultipart("alternative")

    msg["Subject"] = subject
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = to_email

    html_part = MIMEText(html_body, "html")

    msg.attach(html_part)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    sender_email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWORD")


    server.login(sender_email, password)
    
    

    server.sendmail(msg["From"], [msg["To"]], msg.as_string())

    server.quit()