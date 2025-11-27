from selenium.webdriver.common.by import By


class SearchLocators:
    search = (By.XPATH, "//input[@placeholder='Search for Products, Medicine...']")
    auto_suggestions= (By.XPATH, "//div[contains(@class,'cursor-pointer')]/span[last()]")
