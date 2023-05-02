import time

from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from  selenium.webdriver.support import expected_conditions as EC


def test_wait():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/delay/")
    driver.implicitly_wait(30)
    assert 'Delay' in driver.title

    commit = driver.find_element(By.NAME, 'commit')
    commit.click()
    # time.sleep(6)

    # driver.find_element(By.NAME, 'commit1').click()
    # delay_element = driver.find_element(By.ID, 'delay')
    # print('Delay attempt: ' + delay_element.text)

    # element = driver.find_element(By.ID, 'two')
    # el = driver.find_element(By.XPATH, "//h2[@id='two']")
    # print('First attempt: ' + element.text)

    # el = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH("//p[@id='']")), 'Submitted')
    WebDriverWait(driver, 10).until(wait_till_text_appear((By.ID, "two"), 'here!'))
    print('After waiting: ' + driver.find_element(By.ID, 'two').text)
    # el.click()

    time.sleep(3)
    driver.quit()


class wait_till_text_appear:
    def __init__(self, locator_, text_):
        self.locator = locator_
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = driver.find_element(*self.locator).text
            return self.text in element_text
        except BaseException:
            return False
