# pages/base_page.py
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        self.wait_for_element(by, value).click()

    def enter_text(self, by, value, text):
        element = self.wait_for_element(by, value)
        element.clear()
        element.send_keys(text)

    def scroll_to_element_and_click(self, by, value):
        element = self.wait_for_element(by, value)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # self.wait.until(EC.element_to_be_clickable((by, value))).click()
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element(self, by, value):
        element = self.wait_for_element(by, value)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
