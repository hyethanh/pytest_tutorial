import time

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def test_staleexception():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/signup/")
    driver.implicitly_wait(30)
    assert 'Registration' in driver.title

    """
    element = driver.find_element(By.ID, 'username')
    element.click()
    driver.refresh()

    try:
        element.send_keys('hyethanh')
    except StaleElementReferenceException:
        element = driver.find_element(By.ID, 'username')
        element.send_keys('hyethanh1')
    """

    click(driver, (By.ID, 'username'))
    driver.refresh()
    send_key(driver, (By.ID, 'username'), 'HYETHANH')

    click(driver, (By.ID, 'email'))
    send_key(driver, (By.ID, 'email'), 'HYETHANH@gmail.com')

    time.sleep(3)
    driver.quit()


def click(driver, locator):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))


def send_key(driver, locator, value):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).clear()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).send_keys(value)
