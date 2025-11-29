from selenium.webdriver.common.keys import Keys

from page_objects.search.searchProps import SearchProps
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class SearchPage(SearchProps):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_search_text(self, search_text):

        bar = self.wait.until(EC.element_to_be_clickable(self.fill_search_bar))
        bar.clear()
        bar.send_keys(search_text)
        return bar

    def select_first_suggestion(self):
        suggestions = self.suggestions_list

        suggestions[0].click()


    def select_suggestion_by_keyword(self, keyword, timeout=10):
        wait = WebDriverWait(self.driver, timeout)

        def find_and_click(driver):
            # Re-fetch suggestions
            suggestions = self.suggestions_list
            for s in suggestions:
                if keyword.lower() in s.text.strip().lower():
                    s.click()
                    return True
            return False

        wait.until(find_and_click)

# def search_product(self, text, suggestion_to_select=None):
#     """
#     High-level search method:
#     - Type text in the search bar
#     - If suggestion_to_select is given, pick that suggestion
#     - Otherwise, press Enter
#     """
#     bar = self.wait.until(EC.element_to_be_clickable(self.fill_search_bar))
#     bar.click()
#     bar.clear()
#     bar.send_keys(text)
#
#     if suggestion_to_select:
#         for item in self.suggestions_list:
#             if item.text.strip() == suggestion_to_select:
#                 item.click()
#                 return  # Stop after clicking the suggestion
#     else:
#         bar.send_keys(Keys.ENTER)
