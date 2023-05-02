import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Global:
    driver = None


def test_sample():
    Global.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    Global.driver.maximize_window()
    Global.driver.get("https://qavbox.github.io/demo/")
    assert 'QAVBOX' in Global.driver.title


def test_navReg():
    Global.driver.find_element(By.LINK_TEXT, "SignUp Form").click()
    Global.driver.close()
    Global.driver.quit()
