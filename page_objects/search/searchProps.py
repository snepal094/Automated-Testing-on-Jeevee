from page_objects.search.searchLocators import SearchLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchProps(SearchLocators):
    @property
    def fill_search_bar(self):
        return self.driver.find_element(*SearchLocators.search)

    @property
    def container(self):
        # Wait for the suggestions container to be visible first
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SearchLocators.container)
        )

    @property
    def suggestions_list(self):
        # Get the container element first
        container = self.container

        # Define a function to wait for at least one suggestion
        def check_suggestions(c):
            elements = c.find_elements(*SearchLocators.suggestions_list)
            if elements:
                return elements  # Return the list if there is at least one element
            else:
                return False  # Keep waiting if no elements found

        # Wait up to 10 seconds for at least one suggestion
        suggestions = WebDriverWait(container, 10).until(check_suggestions)

        return suggestions
