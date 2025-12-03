import logging
import time

from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from page_objects.cart.CartLocators import CartLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartProps(CartLocators):
    @property
    def add_from_product_page(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartLocators.add_to_cart_from_product_page)
        )

    @property
    def cart_button(self):
        # Wait for overlay to disappear
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "common_backdrop__wapXy"))
        )

        btn= WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartLocators.cart_page_btn)
        )

        # retry click until it succeeds
        timeout = time.time() + 10 # now + 10s
        # So timeout is the latest time we’ll keep retrying before giving up.

        while True: # ends when either clicking the button succeeds, or the timeout limit is reached
            try:
                btn.click()
                break
            except ElementClickInterceptedException: # if smth is blocking the button
                # catches this execption so that we can retry without the program crashing
                if time.time() > timeout:
                    raise TimeoutException("Cart button click blocked by overlay after 10s")
                # time.sleep(0.2) # wait 0.2s before retries to avoid rapid clicking

        return btn


    @property
    def checkout_button(self):

        # wait for toast to disappear ('Logged In Successfully')
        logging.info('Processing Checkout')
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.Toastify__toast-container"))
        )

        # wait until button is clickable
        btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CartLocators.checkout_btn)
        )
        # use ActionChains to move to the element
        ActionChains(self.driver).move_to_element(btn).perform()
        time.sleep(2)
        return btn

    @property
    def remove(self):

        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "common_backdrop__wapXy"))
        )

        # wait for button to be clickable
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartLocators.remove_btn_locator)
        )

    @property
    def confirm_remove(self):
        # wait until button is visible and enabled
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartLocators.confirm_remove_locator)
        )

        # wait until overlay disappears, if any
        try:
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "common_backdrop__wapXy"))
            )
        except TimeoutException:
            logging.warning("Overlay still present, retrying click...")

        # retry clicking until it succeeds or timeout
        timeout = time.time() + 10  # try for 10 seconds
        while True:
            try:
                btn.click()
                logging.info("Item removed from cart successfully")
                break
            except ElementClickInterceptedException:
                if time.time() > timeout:
                    raise TimeoutException("Confirm remove button blocked by overlay after 10s")
                time.sleep(0.2)  # wait before retrying

        return btn

    @property
    def increase_quantity(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CartLocators.incr_qty_locator)
        )

    @property
    def decrease_quantity(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CartLocators.decr_qty_locator)
        )

# Instead of handling this in every property, you can wrap click actions in a helper like:

# def safe_click(self, locator):
#     WebDriverWait(self.driver, 10).until(
#         EC.invisibility_of_element_located((By.CLASS_NAME, "common_backdrop__wapXy"))
#     )
#     element = WebDriverWait(self.driver, 10).until(
#         EC.presence_of_element_located(locator)
#     )
#     timeout = time.time() + 10
#     while True:
#         try:
#             element.click()
#             break
#         except ElementClickInterceptedException:
#             if time.time() > timeout:
#                 raise
#             time.sleep(0.2)
