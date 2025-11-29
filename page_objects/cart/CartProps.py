import time

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from page_objects.cart.CartLocators import CartLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartProps(CartLocators):
    @property
    def add_from_product_page(self):
        return self.driver.find_element(*CartLocators.add_to_cart_from_product_page)

    # @property
    # def cart_button(self):
    #     # return self.driver.find_element(*CartLocators.cart_page_btn)
    #     # wait for overlay to disappear (an invisible element was obstructing the button)
    #     WebDriverWait(self.driver, 10).until(
    #         EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.common_backdrop__wapXy"))
    #     )
    #
    #     return WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(CartLocators.cart_page_btn)
    #         # no * because it unpacks cart_page_btn (By, locator) (we need a single tuple)
    #     )

    @property
    def cart_button(self):
        overlay_selector = (By.CSS_SELECTOR, "div.common_backdrop__wapXy")

        # Wait for overlay to disappear
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(overlay_selector))

        # Wait for cart button to be clickable
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartLocators.cart_page_btn)
        )

        # Scroll to the button
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)

        # Use ActionChains to click safely, retry up to 3 times if intercepted
        for _ in range(3):
            try:
                ActionChains(self.driver).move_to_element(btn).click().perform()
                return btn
            except ElementClickInterceptedException:
                WebDriverWait(self.driver, 1).until(EC.invisibility_of_element_located(overlay_selector))

        # Final attempt without exceptions
        ActionChains(self.driver).move_to_element(btn).click().perform()
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
