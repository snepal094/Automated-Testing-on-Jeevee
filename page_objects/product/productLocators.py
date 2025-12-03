from selenium.webdriver.common.by import By

class ProductLocators:
    product_card = (By.CSS_SELECTOR, "span[class*='products_productCard']")
    # product_card = (By.XPATH, "//span[contains(@class,'products_productCard__TgLt6')]")

