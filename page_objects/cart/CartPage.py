import logging
import time

from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from page_objects.cart.CartProps import CartProps


class CartPage(CartProps):
    def __init__(self, driver):
        self.driver=driver

    def add_to_cart_from_product_page(self):
        logging.info("adding to cart...")
        self.add_from_product_page.click()

    def open_cart_page(self):

        # retry click until it succeeds
        timeout = time.time() + 10 # now + 10s
        # So timeout is the latest time we’ll keep retrying before giving up.

        while True: # ends when either clicking the button succeeds, or the timeout limit is reached
            try:
                self.cart_button.click()
                break
            except ElementClickInterceptedException: # if smth is blocking the button
                # catches this execption so that we can retry without the program crashing
                if time.time() > timeout:
                    raise TimeoutException("Cart button click blocked by overlay after 10s")
                # time.sleep(0.2) # wait 0.2s before retries to avoid rapid clicking

        # self.cart_button.click()
        # logging.info("opening cart page...")

    def checkout(self):
        self.checkout_button.click()
        logging.info("checking out...")

    def remove_from_cart(self):
        self.remove.click()
        self.confirm_remove.click()
        logging.info("removed item from cart")

    def increase_item_count(self):
        self.increase_quantity.click()

        # wait for toast to appear
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(CartProps.toast_locator)
            )
        except:
            logging.info("Processing toast did not appear")

        # Wait for toast to disappear
        try:
            WebDriverWait(self.driver, 15).until(
                EC.invisibility_of_element_located(CartProps.toast_locator)
            )
            logging.info("Processing toast disappeared, item count updated")
        except:
            logging.warning("Processing toast did not appear or already gone")

    def decrease_item_count(self):
        self.decrease_quantity.click()
        logging.info("item count decreased")