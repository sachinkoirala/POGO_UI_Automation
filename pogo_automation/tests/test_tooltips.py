import logging
import time
import pytest
from pogo_automation.pages.home_page import HomePage
from pogo_automation.pages.login_page import LoginPage
from pogo_automation.utils.config import EMAIL, PASSWORD, SS_Path

logging.basicConfig(level=logging.INFO)

@pytest.mark.run(order=4)
def test_tooltips(driver):
    logging.info("Starting test_tooltips")
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    home_page.click_signin()
    logging.info("Clicked Sign In button")
    driver.save_screenshot(SS_Path + "signin_clicked.png")

    login_page.enter_username(EMAIL)
    logging.info("Entered username")
    driver.save_screenshot(SS_Path + "username_entered.png")

    login_page.enter_password(PASSWORD)
    logging.info("Entered password")
    driver.save_screenshot(SS_Path + "password_entered.png")

    assert home_page.is_logged_in() == True
    logging.info("Login successful")
    driver.save_screenshot(SS_Path + "login_successful.png")

    time.sleep(3)

    gem_tooltip = home_page.get_gem_count_tooltip_and_screenshot(SS_Path + "gem_count.png")
    logging.info("Captured gem count tooltip")
    pogi_tooltip = home_page.get_pogis_button_tooltip_and_screenshot(SS_Path + "pogis_button.png")
    logging.info("Captured pogis button tooltip")
    friends_tooltip = home_page.get_friends_icon_tooltip_and_screenshot(SS_Path + "friends_icon.png")
    logging.info("Captured friends icon tooltip")

    assert pogi_tooltip == "Pogi Meter"
    logging.info("Pogi tooltip assertion passed")
    assert gem_tooltip == "Gem Balance"
    logging.info("Gem tooltip assertion passed")
    assert friends_tooltip == "Friends List"
    logging.info("Friends tooltip assertion passed")