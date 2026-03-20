import smtplib
from email.mime.text import MIMEText

def send_email_alert(message):
    sender = "your_email@gmail.com"
    receiver = "receiver@gmail.com"

    msg = MIMEText(message)
    msg["Subject"] = "Dark Web Alert"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, "password")
            server.send_message(msg)
    except Exception as e:
        print("Email failed:", e)