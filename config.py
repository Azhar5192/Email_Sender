from dotenv import load_dotenv
import os

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

