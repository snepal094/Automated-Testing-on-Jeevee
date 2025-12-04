import logging
import time

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

        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartLocators.cart_page_btn)
        )


    @property
    def checkout_button(self):

        # wait for toast to disappear ('Logged In Successfully')
        logging.info('Processing Checkout...')
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
        return btn


    @property
    def increase_quantity(self):
        # Wait for the increment button to be clickable
        incr_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartLocators.incr_qty_locator)
        )
        return incr_btn


    @property
    def decrease_quantity(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CartLocators.decr_qty_locator)
        )


    def manage_toast(self):
        # wait for toast to appear
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(CartLocators.toast_locator)
            )
        except:
            logging.info("Processing toast did not appear")

        # Wait for toast to disappear
        try:
            WebDriverWait(self.driver, 15).until(
                EC.invisibility_of_element_located(CartLocators.toast_locator)
            )
            logging.info("Processing toast disappeared, item count updated")
        except:
            logging.warning("Processing toast did not appear or already gone")
