import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class LoginPage:

    # locators
    user_input = "user-name"
    password_input = "password"
    login_button = "login-button"
    locked_message = "//h3[contains(text(),'Epic sadface: Sorry, this user has been locked out.')]"

    def __init__(self, driver):
        self.driver = driver

    # functions

    def login_page_validation(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.user_input)))
        username_input = self.driver.find_element(By.ID, self.user_input).is_displayed()
        return username_input

    def fill_user_credential(self, username):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.user_input)))
        username_input = self.driver.find_element(By.ID, self.user_input)
        username_input.clear()
        username_input.send_keys(username)

    def fill_pass_credential(self, passw):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.password_input)))
        passw_input = self.driver.find_element(By.ID, self.password_input)
        passw_input.clear()
        passw_input.send_keys(passw)

    def login_action(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.login_button)))
        login_btn = self.driver.find_element(By.ID, self.login_button)
        login_btn.click()

    def is_url_valid(self):
        time.sleep(2)
        url = self.driver.current_url
        if "/inventory" in url:
            return True
        else:
            print(url)
            return False

    def is_locked_alert_dis(self):
        WebDriverWait(self.driver, 20). until(EC.visibility_of_element_located((By.XPATH, self.locked_message)))
        locked_alert = self.driver.find_element(By.XPATH, self.locked_message).is_displayed()
        return locked_alert
