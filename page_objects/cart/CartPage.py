from page_objects.cart.CartProps import CartProps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(CartProps):
    def __init__(self, driver):
        self.driver=driver
        # self.wait = WebDriverWait(driver, 10)

    def add_to_cart_from_product_page(self):
        self.add_from_product_page.click()

    def open_cart_page(self):
        self.cart_button.click()

    def checkout(self):
        self.checkout_button.click()