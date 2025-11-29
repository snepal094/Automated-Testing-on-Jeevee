from page_objects.product.productLocators import ProductLocators

class ProductProps(ProductLocators):
    @property
    def product(self):
        return self.driver.find_element(*ProductLocators.product_card)