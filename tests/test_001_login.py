import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.LoginPage import LoginPage
from helpers.FunctionLib import *


class TestValidLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.helpers = FunctionLib()
        self.op = self.helpers.driver_headless()
        chrome_driver_path = self.helpers.get_chrome_driver()
        self.driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path), options=self.op)
        self.driver.get(self.helpers.get_url_app())
        self.username = self.helpers.user_web_standard()
        self.passw = self.helpers.pass_web()
        self.loginpage = LoginPage(driver=self.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_to_wait=50)

    def test_001_successful_login(self):
        self.loginpage.fill_user_credential(username=self.username)
        self.loginpage.fill_pass_credential(passw=self.passw)
        self.loginpage.login_action()
        is_login_valid = self.loginpage.is_url_valid()
        assert is_login_valid is True, "The login was not successful"

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
