# pages/registration_page.py
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from .base_page import BasePage

class RegistrationPage(BasePage):

    USERNAME_INPUT = (By.ID, "username")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='password']")
    EA_ID_BUTTON = (By.XPATH, "//input[@id='originId']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submitBtn']")
    Reg_Submit_Button = (By.XPATH, "//a[@id='submitBtn']")
    DOB_MONTH = (By.XPATH, "//select[@id='clientreg_dobmonth-selctrl']")
    DOB_DAY = (By.XPATH,"//select[@id='clientreg_dobday-selctrl']")
    DOB_YEAR = (By.XPATH,"//select[@id='clientreg_dobyear-selctrl']")
    Next_Button = (By.XPATH, "//a[@id='countryDobNextBtn']")
    Basic_Info_Next_Button = (By.XPATH, "//a[@id='basicInfoNextBtn']")
    Accept_UA_Button = (By.XPATH, "//label[@for='readAccept']")
    OTP_Input = (By.XPATH, "//input[@id='emailVerifyCode']")
    Sned_OTP_Button = (By.XPATH, "//a[@id='btnSendCode']")
    ScreenName_Input = (By.XPATH, "//input[@id='screenname']")
    Nextt_Button = (By.XPATH, "//div[contains(text(),'Next')]")


    def register(self, email, password, username):
        self.enter_text(*self.EMAIL_INPUT, email)
        self.enter_text(*self.PASSWORD_INPUT, password)
        self.enter_text(*self.EA_ID_BUTTON, username)
        time.sleep(3)
        self.click(*self.Basic_Info_Next_Button)


    def select_dob(self):
        Select(self.wait_for_element(*self.DOB_MONTH)).select_by_index(1)
        Select(self.wait_for_element(*self.DOB_DAY)).select_by_index(1)
        Select(self.wait_for_element(*self.DOB_YEAR)).select_by_index(20)
        self.click(*self.Next_Button)

    def accept_ua(self):
        self.click(*self.Accept_UA_Button)
        self.click(*self.Reg_Submit_Button)

    def enter_otp(self, otp):
        self.enter_text(*self.OTP_Input, otp)
        self.click(*self.Sned_OTP_Button)

    def enter_screenname(self, screenname):
        self.enter_text(*self.ScreenName_Input, screenname)
        self.click(*self.Nextt_Button)