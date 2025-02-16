# utils/email_utils.py
import imaplib
import email
import re
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read variables
email_user = os.getenv('EMAIL_USER')
email_pass = os.getenv('EMAIL_PASS')

def get_otp_from_email(email_address=email_user, password=email_pass):
    # Connect to the Gmail IMAP server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_address, password)
    mail.select("inbox")

    # Search for unread emails
    status, messages = mail.search(None, '(UNSEEN)')
    email_ids = messages[0].split()

    otp = None
    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])

        # Check if the email is multipart
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    otp = extract_otp(body)
                    if otp:
                        break
        else:
            body = msg.get_payload(decode=True).decode()
            otp = extract_otp(body)

        if otp:
            break

    mail.logout()
    return otp

def extract_otp(email_body):
    # Use regex to find the OTP in the email body
    match = re.search(r'\b\d{6}\b', email_body)
    if match:
        return match.group(0)
    return None