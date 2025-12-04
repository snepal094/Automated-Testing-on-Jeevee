import json
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
        self.open_url(self.creds["url"])


        # login = LoginPage(self.driver)
        #
        # login.profile_icon_expand()
        # # time.sleep(5)
        # login.login_page()
        # # time.sleep(5)
        # login.sign_in('', '')
        # # time.sleep(5)


    def teardown_method(self):
        self.driver.quit()

    def open_url(self, url):
        self.driver.get(url)