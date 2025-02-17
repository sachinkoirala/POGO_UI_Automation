# tests/test_registration.py
import logging
import time

import pytest

from pogo_automation.pages.registration_page import RegistrationPage
from pogo_automation.pages.home_page import HomePage
from pogo_automation.utils.email_utils import get_otp_from_email
from pogo_automation.utils.helpers import generate_unique_id, generate_screenname
from pogo_automation.utils.config import EMAIL, PASSWORD, SS_Path
from pogo_automation.utils.recaptcha_solver import solve_recaptcha

logging.basicConfig(level=logging.INFO)

@pytest.mark.run(order=5)
def test_registration(driver):
    logging.info("Starting test_registration")
    registration_page = RegistrationPage(driver)
    home_page = HomePage(driver)

    # Open the registration page
    home_page.click_signin()
    home_page.click_create_account()
    driver.save_screenshot(SS_Path + "createaccount.png")

    # Select DOB
    registration_page.select_dob()
    logging.info("Selected DOB")
    driver.save_screenshot(SS_Path + "dob_selected.png")

    # Fill out the registration form
    username = generate_unique_id()
    registration_page.register(EMAIL, PASSWORD, username)
    driver.save_screenshot(SS_Path + "form_filled.png")

    # Accept UA
    time.sleep(5)
    registration_page.accept_ua()
    driver.save_screenshot(SS_Path + "ua_accepted.png")

    # Enter OTP
    otp = get_otp_from_email()
    assert otp is not None, "Failed to fetch OTP from email"
    logging.info("Fetched OTP from email")

    registration_page.enter_otp(otp)
    logging.info("Entered OTP")
    driver.save_screenshot(SS_Path + "otp_entered.png")

    # Enter screenname
    screenname = generate_screenname()
    registration_page.enter_screenname(screenname)
    driver.save_screenshot(SS_Path + "screenname_entered.png")

    # Solve recaptcha
    # assert solve_recaptcha(driver), "Failed to solve recaptcha"
    # driver.save_screenshot(SS_Path + "recaptcha_solved.png")

    # Verify registration success
    assert "Registration successful" in driver.page_source
    logging.info("Registration successful")
    driver.save_screenshot(SS_Path + "registration_successful.png")

    # Optional: Add a delay to observe the result
    time.sleep(5)