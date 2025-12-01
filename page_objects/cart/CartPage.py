import logging

from page_objects.cart.CartProps import CartProps


class CartPage(CartProps):
    def __init__(self, driver):
        self.driver=driver

    def add_to_cart_from_product_page(self):
        self.add_from_product_page.click()
        logging.info("adding to cart...")

    def open_cart_page(self):
        self.cart_button.click()
        logging.info("opening cart page...")

    def checkout(self):
        self.checkout_button.click()
        logging.info("checking out...")

    def remove_from_cart(self):
        self.remove().click()
        self.confirm_remove().click()
        logging.info("removed item from cart")

    def increase_item_count(self):
        self.increase_quantity.click()
        logging.info("item count increased")

    def decrease_item_count(self):
        self.decrease_quantity.click()
        logging.info("item count decreased")