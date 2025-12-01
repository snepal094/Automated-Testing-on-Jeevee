from selenium.webdriver.common.by import By

class LoginLocators:

    # profile_icon = (By.XPATH, "//div[@class='user_greetings__29Sj5 md:block relative']")
    # BUT — usually Tailwind classes and Webpack-generated classes may change.
    # Also the order of classes can change, so exact match is often fragile.
    # Using the prefix user_greetings__ is much more stable than the random hash 29Sj5
    # use 'contains'

    profile = (By.XPATH, "//div[contains(@class, 'user_greetings__')]")

    login = (By.XPATH, "//div[contains(@class, 'cursor-pointer')]//div[text()='Login']/..")

    mobile_num_input = (By.XPATH, "//input[@name='phone']")
    password_input = (By.XPATH, "//input[@name='password']")
    login_button = (By.XPATH, "//button[normalize-space()='Sign In']")