import smtplib

from config import SENDER_EMAIL, APP_PASSWORD
from config import SMTP_SERVER, SMTP_PORT
from email.message import EmailMessage

def send_email(contact, message):
    try:
        email = EmailMessage() #step 1

        # step 2
        email["From"] = SENDER_EMAIL

        email["To"] = contact["Email"]

        email["Subject"] = "Thank you for contacting Nexora Consultancy"
            
        email.set_content(message)

    

    #step 3 connect
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:

        #step 4 login
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            
            smtp.send_message(email)
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False