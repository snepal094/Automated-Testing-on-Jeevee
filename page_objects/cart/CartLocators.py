from selenium.webdriver.common.by import By


class CartLocators:
    add_to_cart_from_product_page = (By.XPATH, "//button[contains(@class,'btn-product-detail') and contains(text(),'Add to Cart')]")

    # cart_page_btn = (By.XPATH, "//svg[path[contains(@d,'158.3,314.8')]]")

    cart_page_btn = (By.XPATH, '//*[@id="__next"]/div[1]/div/div[1]/div/div[1]/div[2]/div/div[4]/div[2]')

    checkout_btn = (By.XPATH, "//button[contains(text(),'Checkout')]")
