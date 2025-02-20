# utils/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_URL = "https://www.pogo.com"
USERNAME = "AmbikaTest"
EMAIL = os.getenv('EMAIL_USER')
PASSWORD = os.getenv('EMAIL_PASS')
APP_PASSWORD = os.getenv('APP_PASS')
SS_Path = "pogo_automation/tests/Screenshots/"
Reg_Email = os.getenv('REG_EMAIL_USER')
