from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import random
import os
from faker import Faker


class FunctionLib:
    def __init__(self, my_driver=''):
        self.driver = my_driver
        self.url = 'https://'

    @staticmethod
    def get_chrome_driver():
        path_env = os.path.abspath(os.path.join(os.path.join(os.path.join(os.path.dirname(__file__),
                                                                          '..'), 'drivers'), 'chromedriver.exe'))

    @staticmethod
    def driver_headless():
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shadow')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-dev-usage')
        options.add_argument('--disable-notifications')
        return options

    def get_url_app(self):
        # response_url = self.url + name_env + '.saucedemo.com'
        response_url = self.url + 'saucedemo.com'
        return response_url

    @staticmethod
    def user_web_standard():
        load_dotenv()
        user_standard = os.getenv('USER_STANDARD')
        return user_standard

    @staticmethod
    def user_web_locked():
        load_dotenv()
        user_locked = os.getenv('USER_LOCKED')
        return user_locked

    @staticmethod
    def user_web_problem():
        load_dotenv()
        user_problem = os.getenv('USER_PROBLEM')
        return user_problem

    @staticmethod
    def user_web_performance():
        load_dotenv()
        user_performance = os.getenv('USER_PERFORMANCE')
        return user_performance

    @staticmethod
    def user_web_error():
        load_dotenv()
        user_error = os.getenv('USER_ERROR')
        return user_error

    @staticmethod
    def user_web_visual():
        load_dotenv()
        user_visual = os.getenv('USER_VISUAL')
        return user_visual

    @staticmethod
    def pass_web():
        load_dotenv()
        pass_s = os.getenv('PASSWORD')
        return pass_s

    @staticmethod
    def faker_name():
        fake = Faker()
        name = fake.name()
        return name

    @staticmethod
    def faker_last_name():
        fake = Faker()
        last_name = fake.last_name()
        return last_name

    @staticmethod
    def number_random():
        number_rnd = random.randint(1, 100)
        return number_rnd
