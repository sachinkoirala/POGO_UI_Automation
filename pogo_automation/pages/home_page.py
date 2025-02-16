# pages/home_page.py
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    TOOLTIP_LOCATORS = [(By.CSS_SELECTOR, ".tooltip1"), (By.CSS_SELECTOR, ".tooltip2")]
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Search for games']")
    SEARCH_BUTTON = (By.ID, "search_button")
    LOGOUT_BUTTON = (By.XPATH, "//div[contains(text(),'Sign Out')]")
    SignIn_button = (By.XPATH, "(//div[@class='inner__1qxo3'][normalize-space()='Sign In'])")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "(//a[@id='createLink'])")
    LoggedIN_User_IMG = (By.XPATH, "//img[@alt='Avatar Image']")
    LoggedOUT_text = (By.XPATH, "//h1[normalize-space()='Thanks for Playing!']")
    Pogis_Buttton = (By.XPATH, "(//img[@alt='Pogis Icon'])[1]")
    Gem_Count_Button = (By.XPATH, "//img[@alt='Gem Count']")
    Friends_Icon = (By.XPATH, "//img[@alt='Friends Header Navigation Icon']")
    Pogi_Tooltip = (By.XPATH, "//div[contains(text(),'Pogi Meter')]")
    Gem_Tooltip = (By.XPATH, "//div[contains(text(),'Gem Balance')]")
    Friends_Tooltip = (By.XPATH, "//div[contains(text(),'Friends List')]")


    def get_tooltips(self):
        tooltips = []
        for locator in self.TOOLTIP_LOCATORS:
            tooltips.append(self.wait_for_element(*locator).get_attribute("title"))
        return tooltips

    def click_signin(self):
        sign_in_button = self.wait_for_element(*self.SignIn_button)
        self.driver.execute_script("arguments[0].click();", sign_in_button)

    def search_game(self, game_name):
        self.enter_text(*self.SEARCH_INPUT, game_name)
        self.driver.find_element(*self.SEARCH_INPUT).send_keys(Keys.ENTER)

    def logout(self):
        self.click(*self.LoggedIN_User_IMG)
        self.scroll_to_element_and_click(*self.LOGOUT_BUTTON)

    def click_create_account(self):
        self.click(*self.CREATE_ACCOUNT_BUTTON)

    def is_logged_in(self):
        return self.wait_for_element(*self.LoggedIN_User_IMG).is_displayed()

    def is_logged_out(self):
        return self.wait_for_element(*self.LoggedOUT_text).is_displayed()

    def get_pogis_button_tooltip_and_screenshot(self, screenshot_path):
        pogis_button = self.wait_for_element(*self.Pogis_Buttton)
        time.sleep(1)
        # self.driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));", pogis_button)
        ActionChains(self.driver).move_to_element(pogis_button).perform()
        tooltip_text = self.wait_for_element(*self.Pogi_Tooltip).text
        self.driver.save_screenshot(screenshot_path)
        return tooltip_text

    def get_gem_count_tooltip_and_screenshot(self, screenshot_path):
        gem_count_button = self.wait_for_element(*self.Gem_Count_Button)
        time.sleep(1)
        ActionChains(self.driver).move_to_element(gem_count_button).perform()
        tooltip_text = self.wait_for_element(*self.Gem_Tooltip).text
        self.driver.save_screenshot(screenshot_path)
        return tooltip_text


    def get_friends_icon_tooltip_and_screenshot(self, screenshot_path):
        friends_icon = self.wait_for_element(*self.Friends_Icon)
        ActionChains(self.driver).move_to_element(friends_icon).perform()
        time.sleep(1)  # Add a small delay to ensure the tooltip is displayed
        tooltip_text = self.wait_for_element(*self.Friends_Tooltip).text
        self.driver.save_screenshot(screenshot_path)
        return tooltip_text

