from page_objects.cart.CartProps import CartProps


class CartPage(CartProps):
    def __init__(self, driver):
        self.driver=driver

    def add_to_cart_from_product_page(self):
        self.add_from_product_page.click()