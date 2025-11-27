from page_objects.login.loginLocators import LoginLocators


class LoginProps(LoginLocators):
    @property
    def profile_icon(self):
        return self.driver.find_element(*LoginLocators.profile)

    @property
    def login_icon(self):
        return self.driver.find_element(*LoginLocators.login)

    @property
    def mobile_num(self):
        return self.driver.find_element(*LoginLocators.mobile_num_input)

    @property
    def password(self):
        return self.driver.find_element(*LoginLocators.password_input)

    @property
    def sign_in_button(self):
        return self.driver.find_element(*LoginLocators.login_button)