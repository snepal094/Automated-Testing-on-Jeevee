import time

from selenium.webdriver import Keys

from page_objects.cart.CartPage import CartPage
from page_objects.product.ProductPage import ProductPage
from page_objects.search.searchPage import SearchPage
from setup.basetest import BaseTest


class TestWithoutLogin(BaseTest):
    def test_without_login(self):
        search = SearchPage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)

        direct_search= search.enter_search_text("mamaearth sunscreen")
        direct_search.send_keys(Keys.ENTER)
        time.sleep(5)

        product.open_product_page()
        time.sleep(2)
        cart.add_to_cart_from_product_page()
        time.sleep(5)

        print("Login Pop Up appeared")