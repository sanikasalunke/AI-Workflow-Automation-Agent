import smtplib
from email.mime.text import MIMEText
from typing import Dict

def send_email(payload: Dict) -> str:
    """
    payload: {"to": "a@b.com", "from": "...", "subject": "...", "body": "..." }
    For Gmail use App Password or SMTP server credentials.
    """
    to = payload.get("to")
    sender = payload.get("from")
    subject = payload.get("subject", "Automation Agent")
    body = payload.get("body", "")

    if not (to and sender):
        raise ValueError("Missing to/from fields")

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to

    # This example uses Gmail SMTP - update per your SMTP provider
    smtp_host = payload.get("smtp_host", "smtp.gmail.com")
    smtp_port = int(payload.get("smtp_port", 465))
    username = payload.get("smtp_user")
    password = payload.get("smtp_pass")

    if not (username and password):
        raise ValueError("SMTP credentials missing in payload (smtp_user/smtp_pass)")

    with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
        server.login(username, password)
        server.send_message(msg)

    return f"Email sent to {to}"
