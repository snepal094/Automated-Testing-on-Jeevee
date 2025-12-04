import json
import logging
import time

import pytest
from selenium.webdriver import Keys

from page_objects.cart.CartPage import CartPage
from page_objects.login.loginPage import LoginPage
from page_objects.product.productPage import ProductPage
from page_objects.search.searchPage import SearchPage
from setup.basetest import BaseTest


creds_path = r"C:\Users\snepal\PycharmProjects\QA-Project\creds\creds.json"

with open(creds_path, 'r') as f:
    creds = json.load(f)

users = [(u['mobile_num'], u['password']) for u in creds['users']]

class TestWithoutLogin(BaseTest):

    def test_invalid_login(self):
        login = LoginPage(self.driver)
        login.profile_icon_expand()
        login.login_page()
        login.sign_in('0000000000', 'xyzxyzxyz')
        time.sleep(2)
        logging.error('Username and Password not matching.')


    def test_without_login(self):
        search = SearchPage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)

        direct_search= search.enter_search_text("mamaearth sunscreen")
        direct_search.send_keys(Keys.ENTER)
        # time.sleep(5)

        product.open_product_page()
        time.sleep(2)
        cart.add_to_cart_from_product_page()
        time.sleep(5)

        logging.info("Login Pop Up appeared")

    @pytest.mark.parametrize("username,password", users)
    def test_multiple_logins(self, username, password):
        login = LoginPage(self.driver)

        login.profile_icon_expand()
        login.login_page()
        login.sign_in(username, password)
        time.sleep(3)