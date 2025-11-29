from page_objects.cart.CartLocators import CartLocators

class CartProps(CartLocators):
    @property
    def add_from_product_page(self):
        return self.driver.find_element(*CartLocators.cart_from_product_page)