import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, body):

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "prafullsakpali2e@gmail.com"
    msg["To"] = to_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login("prafullsakpali2e@gmail.com", "bagd ylkm gcts hnmi")

    server.sendmail(msg["From"], [msg["To"]], msg.as_string())

    server.quit()