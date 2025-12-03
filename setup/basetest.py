import json
import logging
from selenium.webdriver.common.action_chains import ActionChains


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


from page_objects.login.loginPage import LoginPage

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class BaseTest:
    def setup_method(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("guest")
        prefs={

            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection_enabled": False


        }
        chrome_options.add_experimental_option("prefs",prefs)

        creds_path = r"C:\Users\snepal\PycharmProjects\QA-Project\creds\creds.json"

        with open(creds_path,'r') as f:
            self.creds = json.load(f)

        driver = webdriver.Chrome(options=chrome_options)
        self.driver = driver
        self.driver.maximize_window()
        self.open_url("https://jeevee.com/")


        # login = LoginPage(self.driver)
        #
        # login.profile_icon_expand()
        # # time.sleep(5)
        # login.login_page()
        # # time.sleep(5)
        # login.sign_in('9849956051', 'Jeevee@123')
        # # time.sleep(5)

    def move_mouse_away(self):
        body = self.driver.find_element(By.TAG_NAME, "body") # (0, 0) = top left corner

        window_width = self.driver.execute_script("return window.innerWidth")
        window_height = self.driver.execute_script("return window.innerHeight")

        actions = ActionChains(self.driver)
        # move_to_element_by_offset takes the mouse to the absolute position,
        # rather than a position relative to the current position like move_by_offset
        actions.move_to_element_with_offset(body, 1, 1).perform()
        # 1 and 1 so that the mouse is only almost at the corner

    def teardown_method(self):
        self.driver.quit()

    def open_url(self, url):
        self.driver.get(url)