import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(to_email, subject, html_body):

    msg = MIMEMultipart("alternative")

    msg["Subject"] = subject
    msg["From"] = "prafullsakpali2e@gmail.com"
    msg["To"] = to_email

    html_part = MIMEText(html_body, "html")

    msg.attach(html_part)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()


    server.login("prafullsakpali2e@gmail.com", "bagd ylkm gcts hnmi")

    server.sendmail(msg["From"], [msg["To"]], msg.as_string())

    server.quit()