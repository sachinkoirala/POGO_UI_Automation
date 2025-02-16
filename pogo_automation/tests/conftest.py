import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from webdriver_manager.chrome import ChromeDriverManager
from pogo_automation.utils.config import BASE_URL

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="function")
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(BASE_URL)  # Navigate to the BASE_URL
    driver.maximize_window()
    yield driver
    driver.quit()