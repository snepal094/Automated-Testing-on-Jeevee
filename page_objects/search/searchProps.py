from page_objects.search.searchLocators import SearchLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchProps(SearchLocators):
    @property
    def fill_search_bar(self):
        return self.driver.find_element(*SearchLocators.search)

    @property
    def container(self):
        # Wait for the container to be visible first
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SearchLocators.container)
        )

    @property
    def suggestions_list(self):
        # Wait for the container first
        container = self.container
        # Then wait until at least 1 suggestion is visible inside the container
        suggestions = WebDriverWait(container, 10).until(
            lambda c: c.find_elements(*SearchLocators.suggestions_list)
            if c.find_elements(*SearchLocators.suggestions_list) else False
        )
        return suggestions