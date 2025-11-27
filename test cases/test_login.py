import time

from page_objects.login.loginPage import LoginPage
from page_objects.search.searchPage import SearchPage
from setup.basetest import BaseTest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLogin(BaseTest):
    def test_login(self):
        self.open_url("https://jeevee.com/")

        login= LoginPage(self.driver)
        search = SearchPage(self.driver)

        login.profile_icon_expand()
        time.sleep(5)
        login.login_page()
        time.sleep(5)
        login.sign_in('9849956051', 'Jeevee@123')
        time.sleep(5)

        search.enter_search_text("pilgrim")
        time.sleep(5)
        # search.search_product("pilgrim")
        # time.sleep(5)

