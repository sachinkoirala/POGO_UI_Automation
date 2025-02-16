# pogo_automation/utils/recaptcha_solver.py

import os
import urllib
import pydub
import speech_recognition as sr
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def delay(driver, waiting_time=5):
    driver.implicitly_wait(waiting_time)

def solve_recaptcha(driver):
    try:
        delay(driver)
        frames = driver.find_elements(By.TAG_NAME, "iframe")
        recaptcha_control_frame = None
        recaptcha_challenge_frame = None
        for frame in frames:
            if re.search('reCAPTCHA', frame.get_attribute("title")):
                recaptcha_control_frame = frame
            if re.search('recaptcha challenge', frame.get_attribute("title")):
                recaptcha_challenge_frame = frame
        if not (recaptcha_control_frame and recaptcha_challenge_frame):
            print("[ERR] Unable to find recaptcha. Abort solver.")
            return False

        # Switch to recaptcha frame and click checkbox
        driver.switch_to.frame(recaptcha_control_frame)
        driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()

        # Switch to recaptcha audio control frame
        delay(driver)
        driver.switch_to.default_content()
        driver.switch_to.frame(recaptcha_challenge_frame)

        # Click on audio challenge
        delay(driver)
        driver.find_element(By.ID, "recaptcha-audio-button").click()

        # Get the mp3 audio file
        delay(driver)
        src = driver.find_element(By.ID, "audio-source").get_attribute("src")
        print(f"[INFO] Audio src: {src}")

        path_to_mp3 = "sample.mp3"
        path_to_wav = "sample.wav"

        # Download the mp3 audio file from the source
        urllib.request.urlretrieve(src, path_to_mp3)

        # Load downloaded mp3 audio file as .wav
        sound = pydub.AudioSegment.from_mp3(path_to_mp3)
        sound.export(path_to_wav, format="wav")
        sample_audio = sr.AudioFile(path_to_wav)

        # Translate audio to text with google voice recognition
        delay(driver)
        r = sr.Recognizer()
        with sample_audio as source:
            audio = r.record(source)
        key = r.recognize_google(audio)
        print(f"[INFO] Recaptcha Passcode: {key}")

        # Key in results and submit
        delay(driver)
        driver.find_element(By.ID, "audio-response").send_keys(key.lower())
        driver.find_element(By.ID, "audio-response").send_keys(Keys.ENTER)
        delay(driver)
        driver.switch_to.default_content()
        delay(driver)
        return True
    except Exception as e:
        print(f"[ERR] {e}")
        return False