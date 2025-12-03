from selenium.webdriver import Keys

from page_objects.cart.CartPage import CartPage
from page_objects.login.loginPage import LoginPage
from page_objects.product.productPage import ProductPage
from page_objects.search.searchPage import SearchPage
from setup.basetest import BaseTest


class TestJeeve(BaseTest):
    def test_jeeve(self):
        login = LoginPage(self.driver)
        search = SearchPage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)

        login.profile_icon_expand()
        login.login_page()
        login.sign_in(self.creds["mobile_num"], self.creds["password"])

        direct_search= search.enter_search_text("dot and key sunscreen")
        direct_search.send_keys(Keys.ENTER)

        product.open_product_page()
        cart.add_to_cart_from_product_page()

        cart.open_cart_page()

        cart.increase_item_count()
        cart.decrease_item_count()
        cart.remove_from_cart()

        cart.checkout()