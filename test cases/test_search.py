import time

from page_objects.search.searchPage import SearchPage
from setup.basetest import BaseTest
from selenium.webdriver.common.keys import Keys



class TestSearch(BaseTest):
    def test_search_directly(self):

        search = SearchPage(self.driver)

        direct_search= search.enter_search_text("pilgrim moisturiser") # this function returns the search text
        direct_search.send_keys(Keys.ENTER)
        # time.sleep(5)

    def test_search_first_suggestion(self):
        search = SearchPage(self.driver)

        search.enter_search_text("lip balm")
        search.select_first_suggestion()
        self.move_mouse_away()
        # time.sleep(5)

    def test_search_relevant_suggestion(self):
        search = SearchPage(self.driver)

        search.enter_search_text("face mask")
        search.select_suggestion_by_keyword("mask")
        self.move_mouse_away() #since the cursor obstructed the page (expanded the categories section)
        # time.sleep(5)