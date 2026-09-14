import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()


EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")