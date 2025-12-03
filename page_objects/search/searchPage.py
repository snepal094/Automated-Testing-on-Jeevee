import logging

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
        logging.info('searching...')
        bar = self.wait.until(EC.element_to_be_clickable(self.fill_search_bar))
        bar.clear()
        bar.send_keys(search_text)
        return bar

    def select_first_suggestion(self):
        logging.info('searching...')
        suggestions = self.suggestions_list

        suggestions[0].click()


    def select_suggestion_by_keyword(self, keyword, timeout=10):
        logging.info('searching...')
        wait = WebDriverWait(self.driver, timeout)

        def find_and_click(drive):
            # Refetch suggestions
            suggestions = self.suggestions_list
            for s in suggestions:
                if keyword.lower() in s.text.strip().lower():
                    s.click()
                    return True
            return False

        wait.until(find_and_click)
