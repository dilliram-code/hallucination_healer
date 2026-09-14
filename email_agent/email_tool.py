import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")

def send_email(
    recipient: str,
    subject: str,
    body: str
) -> str:
    """
    Send an email using Gmail SMTP.

    Args:
        recipient: Email address of the recipient.
        subject: Subject of the email.
        body: Full email body.

    Returns:
        A message describing whether the email was sent.
    """

    if not EMAIL_ADDRESS:
        return "Error: EMAIL_ADDRESS is not configured."

    if not EMAIL_APP_PASSWORD:
        return "Error: EMAIL_APP_PASSWORD is not configured."

    # Create the email
    message = EmailMessage()

    message["From"] = EMAIL_ADDRESS
    message["To"] = recipient
    message["Subject"] = subject

    message.set_content(body)
    
    try:

        # Connect to Gmail SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:

            # Upgrade connection to encrypted TLS
            server.starttls()

            # Login
            server.login(
                EMAIL_ADDRESS,
                EMAIL_APP_PASSWORD
            )

            # Send email
            server.send_message(message)

        return f"Email successfully sent to {recipient}"
      
    except Exception as e:
        return f"Failed to send email: {str(e)}"