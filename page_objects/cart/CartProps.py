import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from page_objects.cart.CartLocators import CartLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartProps(CartLocators):
    @property
    def add_from_product_page(self):
        return self.driver.find_element(*CartLocators.add_to_cart_from_product_page)

    @property
    def cart_button(self):
        btn= WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartLocators.cart_page_btn)
        )
        return btn


    @property
    def checkout_button(self):

        # wait for toast to disappear ('Logged In Successfully')
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.Toastify__toast-container"))
        )

        # wait until button is clickable
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartLocators.checkout_btn)
        )
        # use ActionChains to move to the element
        ActionChains(self.driver).move_to_element(btn).perform()
        time.sleep(2)
        return btn

    def remove(self):
        # wait for button to be clickable
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartLocators.remove_btn_locator)
        )

    def confirm_remove(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartLocators.confirm_remove_locator)
        )

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