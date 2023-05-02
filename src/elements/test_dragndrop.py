import time

from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_dragndrop():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/dragndrop/")
    assert 'DragnDrop' in driver.title

    action = ActionChains(driver)
    source = driver.find_element(By.ID, 'draggable')
    target = driver.find_element(By.ID, 'droppable')
    action.drag_and_drop(source, target).perform()
    time.sleep(3)
    driver.save_screenshot('./pytest_tutorial/screenshots/images/dragndrop.png')

    driver.quit()
