import pytest

import time


from page_objects.login.loginPage import LoginPage
from setup.basetest import BaseTest

users= [("9849956051", "Jeevee@123"), ("9843368866", "Ouw7Y1zR-b-DhGs"), ("0987654321", "invalid-password")]

class TestUsers(BaseTest):
    @pytest.mark.parametrize("username,password", users)
    def test_demo(self, username, password):
        login = LoginPage(self.driver)

        login.profile_icon_expand()
        login.login_page()
        login.sign_in(username, password)

        time.sleep(10)