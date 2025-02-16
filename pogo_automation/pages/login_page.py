# pages/login_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):

    USERNAME_INPUT = (By.XPATH, "//input[@id='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    LOGIN_BUTTON = (By.XPATH, "//a[@id='logInBtn']")
    CreateAccount_button = (By.XPATH, "//a[@id='createLink']")

    # def login(self, username, password):
    #     self.enter_text(*self.USERNAME_INPUT, username)
    #     self.enter_text(*self.PASSWORD_INPUT, password)
    #     self.click(*self.LOGIN_BUTTON

    def enter_username(self, username):
        self.enter_text(*self.USERNAME_INPUT, username)
        self.click(*self.LOGIN_BUTTON)

    def enter_password(self, password):
        self.enter_text(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)


    def click_create_account(self):
        self.click(*self.CreateAccount_button)
