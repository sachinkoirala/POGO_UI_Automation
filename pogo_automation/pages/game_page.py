# pages/game_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class GamePage(BasePage):
    PLAY_NOW_BUTTON = (By.ID, "play_now")
    No_Result_text = (By.XPATH, "//ul[contains(.,'Make sure you're using correct spelling.')]")
    solitaire_game_tile = (By.XPATH, "//a[normalize-space()='Snowbird Solitaire']")
    Play_Now_button = (By.XPATH, "(//div[normalize-space()='Play Now'])")



    def is_play_now_button_present(self):
            return self.wait_for_element(*self.PLAY_NOW_BUTTON).is_displayed()

    def is_no_result_text_present(self):
            return self.wait_for_element(*self.No_Result_text).is_displayed()

    def click_solitaire_game_tile(self):
        self.click(*self.solitaire_game_tile)

    def is_play_now_button_present(self):
        return self.wait_for_element(*self.Play_Now_button).is_displayed()

