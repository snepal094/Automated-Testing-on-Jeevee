from page_objects.login.loginProps import LoginProps


class LoginPage(LoginProps):
    def __init__(self, driver):
        self.driver = driver

    def profile_icon_expand(self):
        self.profile_icon.click()

    def login_page(self):
        self.login_icon.click()

    def sign_in(self, mobile_number, password):
        self.mobile_num.send_keys(mobile_number)
        self.password.send_keys(password)
        self.sign_in_button.click()
