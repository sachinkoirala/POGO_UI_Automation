import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pogo_automation.pages.login_page import LoginPage
from pogo_automation.pages.home_page import HomePage
from pogo_automation.utils.config import EMAIL, PASSWORD, SS_Path

logging.basicConfig(level=logging.INFO)

@pytest.mark.run(order=2)
def test_login_logout(driver):
    logging.info("Starting test_login_logout")
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    home_page.click_signin()
    logging.info("Clicked Sign In button")
    driver.save_screenshot(SS_Path + "signin_clicked.png")

    login_page.enter_username(EMAIL)
    logging.info("Entered username")
    driver.save_screenshot(SS_Path + "username_entered.png")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "password")))
    login_page.enter_password(PASSWORD)
    logging.info("Entered password")
    driver.save_screenshot(SS_Path + "password_entered.png")

    assert home_page.is_logged_in() == True
    logging.info("Login successful")
    driver.save_screenshot(SS_Path + "login_successful.png")

    home_page.logout()
    logging.info("Clicked logout")
    driver.save_screenshot(SS_Path + "logout_clicked.png")

    assert home_page.is_logged_out() == True
    logging.info("Logout successful")
    driver.save_screenshot(SS_Path + "logout_successful.png")