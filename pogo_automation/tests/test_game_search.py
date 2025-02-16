import logging
import time

import pytest

from pogo_automation.pages.home_page import HomePage
from pogo_automation.pages.game_page import GamePage
from pogo_automation.pages.login_page import LoginPage
from pogo_automation.utils.config import EMAIL, PASSWORD, SS_Path

logging.basicConfig(level=logging.INFO)

@pytest.mark.run(order=3)
def test_game_search(driver):
    logging.info("Starting test_game_search")
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    game_page = GamePage(driver)

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
    home_page.search_game("Solitaire")
    logging.info("Searched for game 'Solitaire'")
    driver.save_screenshot(SS_Path + "game_searched.png")

    time.sleep(3)
    game_page.click_solitaire_game_tile()
    logging.info("Clicked Solitaire game tile")
    driver.save_screenshot(SS_Path + "solitaire_game_clicked.png")

    assert game_page.is_play_now_button_present() == True
    logging.info("Play Now button is present")
    driver.save_screenshot(SS_Path + "play_now_button_present.png")