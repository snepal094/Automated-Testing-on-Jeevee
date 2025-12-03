import json

import pytest

import time

from page_objects.login.loginPage import LoginPage
from setup.basetest import BaseTest


creds_path = r"C:\Users\snepal\PycharmProjects\QA-Project\creds\creds.json"

with open(creds_path, 'r') as f:
    creds = json.load(f)

users = [(u['mobile_num'], u['password']) for u in creds['users']]

class TestUsers(BaseTest):
    @pytest.mark.parametrize("username,password", users)
    def test_demo(self, username, password):
        login = LoginPage(self.driver)

        login.profile_icon_expand()
        login.login_page()
        login.sign_in(username, password)

        # time.sleep(10)