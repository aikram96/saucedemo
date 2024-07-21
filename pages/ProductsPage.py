from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class ProductsPage:
    # locators
    products_title = "//span[contains(text(),'Products')]"
    cart_icon = "shopping_cart_container"
    checkout_button = "checkout"
    first_name_input = "first-name"
    last_name_input = "last-name"
    postal_code_input = "postal-code"
    continue_button = "continue"
    checkout_overview_title = "//span[contains(text(),'Checkout: Overview')]"
    finish_button = "finish"
    hamburger_menu_icon = "//button[contains(text(),'Open Menu')]"
    logout_button = "//a[contains(text(),'Logout')]"
    back_to_products_button = "back-to-products"
    order_confirmation = "//h2[contains(text(),'Thank you for your order!')]"
    change_sort_icon = "//select[contains(.,'Name (A to Z)')]"
    add_cart_jacket = "add-to-cart-sauce-labs-fleece-jacket"
    add_cart_onesie = "add-to-cart-sauce-labs-onesie"
    remove_onesie = "remove-sauce-labs-onesie"
    remove_jacket = "remove-sauce-labs-fleece-jacket"

    def __init__(self, driver):
        self.driver = driver

    # functions

    def validate_products_page(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.products_title)))
        products = self.driver.find_element(By.XPATH, self.products_title).is_displayed()
        return products

    def add_to_cart(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.cart_icon)))
        cart_button = self.driver.find_element(By.ID, self.cart_icon)
        cart_button.click()

    def checkout_product(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.checkout_button)))
        checkout_icon = self.driver.find_element(By.ID, self.checkout_button)
        checkout_icon.click()

    def fill_information_required(self, first_name, last_name, postal_code):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.first_name_input)))
        input_first_name = self.driver.find_element(By.ID, self.first_name_input)
        input_first_name.send_keys(first_name)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.last_name_input)))
        input_last_name = self.driver.find_element(By.ID, self.last_name_input)
        input_last_name.send_keys(last_name)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.postal_code_input)))
        input_postal_code = self.driver.find_element(By.ID, self.postal_code_input)
        input_postal_code.send_keys(postal_code)

    def continue_action(self):
        continue_icon = self.driver.find_element(By.ID, self.continue_button)
        continue_icon.click()

    def checkout_overview_validation(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.checkout_overview_title)))
        checkout_overview_title = self.driver.find_element(By.XPATH, self.checkout_overview_title).is_displayed()
        return checkout_overview_title

    def finish_product(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.finish_button)))
        finish_icon = self.driver.find_element(By.ID, self.finish_button)
        finish_icon.click()

    def is_order_completed(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                               self.order_confirmation)))
        order_conf = self.driver.find_element(By.XPATH, self.order_confirmation).is_displayed()
        return order_conf

    def back_product_page(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, self.back_to_products_button)))
        back_product_btn = self.driver.find_element(By.ID, self.back_to_products_button)
        back_product_btn.click()

    def hamburger_menu_action(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.hamburger_menu_icon)))
        hamburger_menu_button = self.driver.find_element(By.XPATH, self.hamburger_menu_icon)
        hamburger_menu_button.click()

    def logout_action(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.logout_button)))
        logout_icon = self.driver.find_element(By.XPATH, self.logout_button)
        logout_icon.click()

    def change_product_sort(self, sort_value):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.change_sort_icon)))
        select_sort_button = self.driver.find_element(By.XPATH, self.change_sort_icon)
        select_sort_button.click()
        select_sort = Select(select_sort_button)
        select_sort.select_by_value(sort_value)

    def sort_validation(self, sort_value_name):
        sort_valid = "//span[contains(text(),'" + str(sort_value_name) + "')]"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, sort_valid)))
        sort_v = self.driver.find_element(By.XPATH, sort_valid).is_displayed()
        return sort_v

    def get_prices(self):
        prices = []
        inventory_items = self.driver.find_elements(By.CSS_SELECTOR,
                                                    "#inventory_container .inventory_list .inventory_item")

        for item in inventory_items:
            price_element = item.find_element(By.CSS_SELECTOR, ".pricebar .inventory_item_price")
            price = price_element.text
            prices.append(price)

        return prices

    def print_prices(self):
        prices = self.get_prices()
        for price in prices:
            print(price)

    def add_single_product(self, id_prod):
        product = "add-to-cart-sauce-labs-" + str(id_prod)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, product)))
        add_to_cart_button = self.driver.find_element(By.ID, product)
        add_to_cart_button.click()

    def remove_button_validation(self, id_prod):
        remove = "remove-sauce-labs-" + str(id_prod)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, remove)))
        remove_valid = self.driver.find_element(By.ID, remove).is_enabled()
        return remove_valid

    def get_selected_prices(self):
        selected_products = [
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie"
        ]
        prices = []

        for product in selected_products:
            try:
                product_container = self.driver.find_element(By.XPATH,
                                                             f"//div[contains(text(),"
                                                             f"'{product}')]/ancestor::div[contains(@class,"
                                                             f" 'inventory_item')]")
                price_element = product_container.find_element(By.CSS_SELECTOR, ".inventory_item_price")
                price = price_element.text
                prices.append((product, price))
            except Exception as e:
                print(f"Not possible to find the product for {product}. Error: {e}")
        self.selected_prices = prices
        return prices

    def print_selected_prices(self):
        prices = self.get_selected_prices()
        for product, price in prices:
            print(f"Product: {product} - Price: {price}")

    def get_cart_badge_value(self):
        try:
            cart_badge_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.shopping_cart_link .shopping_cart_badge"))
            )
            cart_badge_value = cart_badge_element.text
            print(f"Badge found is {cart_badge_value}")
        except Exception as e:
            print(f"Not able to obtain the badge of the cart. Error: {e}")
            return None

    def get_prices_cart(self):
        prices = []
        cart_items = self.driver.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
        for item in cart_items:
            price_element = item.find_element(By.CSS_SELECTOR, ".item_pricebar .inventory_item_price")
            price = price_element.text
            prices.append(price)
        self.cart_prices = prices
        return prices

    def print_prices_cart(self):
        prices = self.get_prices_cart()
        for price in prices:
            print(price)

    def compare_prices(self):
        selected_prices = [price for _, price in self.selected_prices]
        cart_prices = self.cart_prices
        return sorted(selected_prices) == sorted(cart_prices)

    def remove_action(self, id_prod):
        remove = "remove-sauce-labs-" + str(id_prod)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, remove)))
        remove_button = self.driver.find_element(By.ID, remove)
        remove_button.click()

    def get_quantity_cart(self):
        quantities = []
        cart_items = self.driver.find_elements(By.CSS_SELECTOR, ".cart_list .cart_item")
        for item in cart_items:
            quantity_element = item.find_element(By.CSS_SELECTOR, ".cart_quantity")
            quantity = quantity_element.text
            quantities.append(quantity)
        self.cart_quantities = quantities
        return quantities

    def print_quantities_cart(self):
        quantities = self.get_quantity_cart()
        for quantity in quantities:
            print(quantity)

    def get_item_total(self):
        try:
            total_element = self.driver.find_element(By.CSS_SELECTOR, ".summary_subtotal_label")
            item_total = total_element.text
            return item_total
        except Exception as e:
            print(f"The total number of items could not be obtained. Error: {e}")
            return None

    def print_item_total(self):
        item_total = self.get_item_total()
        print(item_total)

    def compare_prices_cart(self):
        selected_prices = [price for _, price in self.selected_prices]
        cart_prices = self.cart_prices
        return sorted(selected_prices) == sorted(cart_prices)
