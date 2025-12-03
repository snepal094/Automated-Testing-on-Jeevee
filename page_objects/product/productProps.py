from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from page_objects.product.productLocators import ProductLocators

class ProductProps(ProductLocators):
    @property
    def product(self):
        # return WebDriverWait(self.driver, 10).until()
        #     (
            # self.driver.find_element(*ProductLocators.product_card))
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ProductLocators.product_card)
)