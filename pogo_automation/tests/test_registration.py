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

    # Fill out the registration form
    registration_page.enter_username(generate_unique_id("testuser"))
    registration_page.enter_password(PASSWORD)
    registration_page.enter_email(EMAIL)
    driver.save_screenshot(SS_Path + "form_filled.png")

    # Solve recaptcha
    assert solve_recaptcha(driver), "Failed to solve recaptcha"
    driver.save_screenshot(SS_Path + "recaptcha_solved.png")

    # Submit the registration form
    registration_page.submit_form()
    driver.save_screenshot(SS_Path + "form_submitted.png")

    # Fetch OTP from email
    otp = get_otp_from_email()
    assert otp is not None, "Failed to fetch OTP from email"
    logging.info("Fetched OTP from email")
    driver.save_screenshot(SS_Path + "otp_fetched.png")

    # Enter OTP
    registration_page.enter_otp(otp)
    logging.info("Entered OTP")
    driver.save_screenshot(SS_Path + "otp_entered.png")

    # Verify registration success
    assert "Registration successful" in driver.page_source
    logging.info("Registration successful")
    driver.save_screenshot(SS_Path + "registration_successful.png")

    # Optional: Add a delay to observe the result
    time.sleep(5)