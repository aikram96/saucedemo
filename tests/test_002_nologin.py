import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.LoginPage import LoginPage
from helpers.FunctionLib import *


class TestInvalidLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.helpers = FunctionLib()
        self.op = self.helpers.driver_headless()
        chrome_driver_path = self.helpers.get_chrome_driver()
        self.driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path), options=self.op)
        self.driver.get(self.helpers.get_url_app())
        self.username = self.helpers.user_web_locked()
        self.passw = self.helpers.pass_web()
        self.loginpage = LoginPage(driver=self.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_to_wait=50)

    def test_001_unsuccessful_login(self):
        self.loginpage.fill_user_credential(username=self.username)
        self.loginpage.fill_pass_credential(passw=self.passw)
        self.loginpage.login_action()
        is_locked_alert_displayed = self.loginpage.is_locked_alert_dis()
        assert is_locked_alert_displayed is True, "Alert: The locked account was able to login"

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
