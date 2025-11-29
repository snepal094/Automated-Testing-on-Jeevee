from selenium.webdriver.common.by import By


class CartLocators:
    cart_from_product_page = (By.XPATH, "//button[contains(@class,'btn-product-detail') and contains(text(),'Add to Cart')]")