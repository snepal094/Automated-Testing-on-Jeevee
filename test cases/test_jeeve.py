import time

from page_objects.cart.CartPage import CartPage
from page_objects.product.ProductPage import ProductPage
from page_objects.search.searchPage import SearchPage
from setup.basetest import BaseTest
from selenium.webdriver.common.keys import Keys


class TestLogin(BaseTest):
    def test_login(self):

        search = SearchPage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)

        #
        # direct_search= search.enter_search_text("pilgrim moisturiser") # this function returns the search text
        # direct_search.send_keys(Keys.ENTER)
        # time.sleep(5)
        #
        # product.open_product_page()
        # time.sleep(2)
        #
        # cart.add_to_cart_from_product_page()
        # time.sleep(2)

        cart.open_cart_page()
        cart.checkout()
        time.sleep(4)

        # self.open_url("https://jeevee.com/")

        # direct_search= search.enter_search_text("mamaearth sunscreen")
        # direct_search.send_keys(Keys.ENTER)
        # time.sleep(5)
        #
        # product.open_product_page()
        # time.sleep(2)
        # cart.add_to_cart_from_product_page()
        # time.sleep(5)
        #
        # self.open_url("https://jeevee.com")

        # search.enter_search_text("lip balm")
        # search.select_first_suggestion()
        # self.move_mouse_away()
        # time.sleep(5)
        #
        # product.open_product_page()
        # time.sleep(2)
        # cart.add_to_cart_from_product_page()
        # time.sleep(5)

        # search.enter_search_text("face mask")
        # search.select_suggestion_by_keyword("mask")
        # self.move_mouse_away() #since the cursor obstructed the page
        # time.sleep(5)
        #
        # product.open_product_page()
        # time.sleep(2)
        # cart.add_to_cart_from_product_page()
        # time.sleep(5)

