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
        self.lastname = self.helpers.faker_last_name()
        self.postalcode = self.helpers.number_random()
        self.driver.maximize_window()
        self.driver.implicitly_wait(time_to_wait=50)
        self.value_srt = "lohi"
        self.srt_value_name = "Price (low to high)"

    def test_001_successful_login(self):
        self.loginpage.fill_user_credential(username=self.username)
        self.loginpage.fill_pass_credential(passw=self.passw)
        self.loginpage.login_action()
        is_login_valid = self.loginpage.is_url_valid()
        assert is_login_valid is True, "The login was not successful"

    def test_002_products(self):
        is_products_page_valid = self.productspage.validate_products_page()
        assert is_products_page_valid is True, "The product page was not valid"
        self.productspage.change_product_sort(sort_value=self.value_srt)
        is_sort_displayed = self.productspage.sort_validation(sort_value_name=self.srt_value_name)
        assert is_sort_displayed is True, "The sort was not implemented"
        self.productspage.print_prices()

    def test_003_multiple_actions_in_products(self):
        self.productspage.add_single_product(id_prod="fleece-jacket")
        self.productspage.add_single_product(id_prod="onesie")
        is_remove_enabled = self.productspage.remove_button_validation(id_prod="fleece-jacket")
        assert is_remove_enabled is True, "The remove was not enabled"
        is_remove_enabled = self.productspage.remove_button_validation(id_prod="onesie")
        assert is_remove_enabled is True, "The remove was not enabled"
        self.productspage.print_selected_prices()
        self.productspage.get_cart_badge_value()
        self.productspage.add_to_cart()

    def test_004_actions_in_carts(self):
        self.productspage.print_prices_cart()
        are_prices_matching = self.productspage.compare_prices()
        assert are_prices_matching is True, "The prices were not matched"
        self.productspage.remove_action(id_prod="onesie")
        self.productspage.get_quantity_cart()
        self.productspage.print_quantities_cart()
        self.productspage.get_cart_badge_value()
        self.productspage.checkout_product()
        self.productspage.fill_information_required(first_name=self.firstname, last_name=self.lastname,
                                                    postal_code=self.postalcode)
        self.productspage.continue_action()
        self.productspage.get_item_total()
        self.productspage.print_item_total()
        are_prices_matching = self.productspage.compare_prices_cart()
        assert are_prices_matching is True, "The prices were not matched"
        self.productspage.finish_product()
        is_order_valid_completed = self.productspage.is_order_completed()
        assert is_order_valid_completed is True, "The order was not possible to complete"

    def test_005_successful_logout_action(self):
        self.productspage.hamburger_menu_action()
        self.productspage.logout_action()
        is_login_page_displayed = self.loginpage.login_page_validation()
        assert is_login_page_displayed is True, "The login page was not displayed"

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
