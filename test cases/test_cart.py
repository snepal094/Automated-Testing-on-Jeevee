import logging
import time

from page_objects.cart.CartPage import CartPage
from page_objects.product.ProductPage import ProductPage
from page_objects.search.searchPage import SearchPage
from setup.basetest import BaseTest
from selenium.webdriver.common.keys import Keys


class TestCart(BaseTest):

    def search_and_add_to_cart_from_product_page(self):

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

    def add_to_cart_from_home_page(self):
        pass

    def open_cart_page(self):
        cart = CartPage(self.driver)

        cart.open_cart_page()
        time.sleep(3)

    def checkout(self):
        cart = CartPage(self.driver)

        cart.open_cart_page()
        cart.checkout()
        time.sleep(3)

    def test_remove_cart_item(self):
        cart = CartPage(self.driver)
        cart.open_cart_page()
        time.sleep(5)
        cart.remove_from_cart()
        time.sleep(5)

    def test_increase_item_count(self):
        cart = CartPage(self.driver)
        cart.open_cart_page()
        time.sleep(5)
        cart.increase_item_count()
        time.sleep(5)

    def test_decrease_item_count(self):
        cart = CartPage(self.driver)
        cart.open_cart_page()
        time.sleep(5)
        cart.decrease_item_count()
        time.sleep(5)