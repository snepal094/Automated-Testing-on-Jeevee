from page_objects.search.searchProps import SearchProps
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(SearchProps):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_search_text(self, search_text):
        """Click → clear → type into search bar"""
        bar = self.wait.until(EC.element_to_be_clickable(self.search_bar))
        bar.click()
        bar.clear()
        bar.send_keys(search_text)

    # def select_suggestion(self, suggestion_text):
    #     """Select an item from autosuggestions dropdown (if present)."""
    #
    #     try:
    #         suggestions = self.autosuggestions  # defined in props
    #     except:
    #         return False
    #
    #     for item in suggestions:
    #         if item.text.strip() == suggestion_text:
    #             item.click()
    #             return True
    #
    #     return False
    #
    # def search_product(self, product_name, suggestion_to_select=None):
    #     """
    #     High-level search function:
    #     - Type in search bar
    #     - Optionally pick a suggestion
    #     """
    #     self.enter_search_text(product_name)
    #
    #     if not product_name.strip():
    #         print("Empty search text")
    #         return
    #
    #     if suggestion_to_select:
    #         self.select_suggestion(suggestion_to_select)
