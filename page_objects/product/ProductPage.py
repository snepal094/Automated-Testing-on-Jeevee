from page_objects.product.productProps import ProductProps


class ProductPage(ProductProps):
    def __init__(self, driver):
        self.driver = driver

    def open_product_page(self):
        self.product.click()