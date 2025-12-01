from selenium.webdriver.common.by import By


class CartLocators:
    add_to_cart_from_product_page = (By.XPATH, "//button[contains(@class,'btn-product-detail') and contains(text(),'Add to Cart')]")

    cart_page_btn= (By.CSS_SELECTOR, "div.cursor-pointer.relative.pr-2.shrink-0")

    checkout_btn = (By.XPATH, "//button[contains(text(),'Checkout')]")

    remove_btn_locator = (By.XPATH,
                          "//button[contains(@class,'cursor-pointer') and .//span[contains(@class,'text-error-500')]]")

    confirm_remove_locator = (By.XPATH,
                          "//button[contains(@class,'btn') and contains(@class,'btn-secondary') and text()='Remove']")

    incr_qty_locator= (By.CSS_SELECTOR, "div.rounded-full.bg-tPrimary-300.p-1.cursor-pointer:last-of-type")

    decr_qty_locator= (By.CSS_SELECTOR, "div.rounded-full.bg-tPrimary-300.p-1.cursor-pointer")
