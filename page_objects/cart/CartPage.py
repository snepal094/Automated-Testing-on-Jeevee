import time

from selenium.webdriver import ActionChains

from page_objects.cart.CartProps import CartProps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(CartProps):
    def __init__(self, driver):
        self.driver=driver

    def add_to_cart_from_product_page(self):
        self.add_from_product_page.click()

    def open_cart_page(self):
        self.cart_button.click()

    def checkout(self):
        self.checkout_button.click()

    def remove_from_cart(self):
        self.remove().click()
        self.confirm_remove().click()

    def increase_item_count(self):
        self.increase_quantity.click()

    def decrease_item_count(self):
        self.decrease_quantity.click()