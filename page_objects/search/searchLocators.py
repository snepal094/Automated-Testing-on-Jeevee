from selenium.webdriver.common.by import By


class SearchLocators:
    search = (By.XPATH, "//input[@placeholder='Search for Products, Medicine...']")

    container = (By.XPATH,
                 "//div[contains(@class,'absolute') and contains(@class,'top-[46px]') and contains(@class,'z-regular')]")

    suggestions_list = (By.XPATH, ".//div[contains(@class,'cursor-pointer')]/span[@class='self-center']")