import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_jeeve():
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://jeevee.com/")

    time.sleep(5)

    driver.quit()