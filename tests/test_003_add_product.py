import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
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
        self.productspage = ProductsPage(driver=self.driver)
        self.firstname = self.helpers.faker_name()
        self.lastname = self.helpers.faker_name()
        self.postalcode = self.helpers.number_random()
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_to_wait=50)

    def test_001_successful_login(self):
        self.loginpage.fill_user_credential(username=self.username)
        self.loginpage.fill_pass_credential(passw=self.passw)
        self.loginpage.login_action()
        is_login_valid = self.loginpage.is_url_valid()
        assert is_login_valid is True, "The login was not successful"

    def test_002_products(self):
        is_products_page_valid = self.productspage.validate_products_page()
        assert is_products_page_valid is True, "The product page was not valid"
        self.productspage.add_single_product(id_prod="bike-light")
        self.productspage.add_to_cart()
        self.productspage.checkout_product()
        self.productspage.fill_information_required(first_name=self.firstname, last_name=self.lastname,
                                           postal_code=self.postalcode)
        self.productspage.continue_action()
        is_checkout_overview_valid = self.productspage.checkout_overview_validation()
        assert is_checkout_overview_valid is True, "The checkout overview was not valid"
        self.productspage.finish_product()
        is_order_valid_completed = self.productspage.is_order_completed()
        assert is_order_valid_completed is True, "The order was not possible to complete"

    def test_003_successful_logout_action(self):
        self.productspage.back_product_page()
        self.productspage.hamburger_menu_action()
        self.productspage.logout_action()
        is_login_page_displayed = self.loginpage.login_page_validation()
        assert is_login_page_displayed is True, "The login page was not displayed"

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
