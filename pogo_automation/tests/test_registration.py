import logging
import time

import pytest

from pogo_automation.pages.registration_page import RegistrationPage
from pogo_automation.pages.home_page import HomePage
from pogo_automation.utils.email_utils import get_otp_from_email
from pogo_automation.utils.helpers import generate_unique_id
from pogo_automation.utils.config import EMAIL, PASSWORD, SS_Path
from pogo_automation.utils.recaptcha_solver import solve_recaptcha

logging.basicConfig(level=logging.INFO)

@pytest.mark.skip(reason="Skipping registration test")
@pytest.mark.run(order=5)
def test_registration(driver):
    logging.info("Starting test_registration")
    registration_page = RegistrationPage(driver)
    home_page = HomePage(driver)

    home_page.click_signin()
    logging.info("Clicked Sign In button")
    driver.save_screenshot(SS_Path + "signin_clicked.png")

    home_page.click_create_account()
    logging.info("Clicked Create Account button")
    driver.save_screenshot(SS_Path + "create_account_clicked.png")

    registration_page.select_dob()
    logging.info("Selected Date of Birth")
    driver.save_screenshot(SS_Path + "dob_selected.png")

    unique_id = generate_unique_id()
    registration_page.register(unique_id, EMAIL, PASSWORD)
    logging.info("Entered registration details")
    driver.save_screenshot(SS_Path + "registration_details_entered.png")

    time.sleep(10)

    is_checked = solve_recaptcha(driver)
    assert is_checked, "Failed to solve reCAPTCHA V2"
    logging.info("Solved reCAPTCHA V2")
    driver.save_screenshot(SS_Path + "recaptcha_solved.png")

    registration_page.accept_ua()
    logging.info("Accepted User Agreement")
    driver.save_screenshot(SS_Path + "ua_accepted.png")

    otp = get_otp_from_email()
    assert otp is not None, "Failed to fetch OTP from email"
    logging.info("Fetched OTP from email")
    driver.save_screenshot(SS_Path + "otp_fetched.png")

    registration_page.enter_otp(otp)
    logging.info("Entered OTP")
    driver.save_screenshot(SS_Path + "otp_entered.png")

    logging.info("Registration successful")
    driver.save_screenshot(SS_Path + "registration_successful.png")

    time.sleep(300)