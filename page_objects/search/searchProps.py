from page_objects.search.searchLocators import SearchLocators


class SearchProps(SearchLocators):
    @property
    def search_bar(self):
        return self.driver.find_element(*SearchLocators.search)

    @property
    def autosuggestions(self):
        return self.driver.find_elements(*SearchLocators.auto_suggestions)