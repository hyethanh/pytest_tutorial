import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_actionchains():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/signup/")
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(50)
    assert 'Registration' in driver.title

    action = ActionChains(driver)
    """
    element = driver.find_element(By.ID, 'username')
    action.click(element).perform()

    action.send_keys('hyethanh').perform()
    time.sleep(2)

    action.send_keys_to_element(element, 'HYETHANH').perform()
    time.sleep(2)
    """

    """
    driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
    right_click_element = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
    action.context_click(right_click_element).send_keys(Keys.ARROW_DOWN).pause(2)\
        .send_keys(Keys.ARROW_DOWN).pause(1).send_keys(Keys.ENTER).perform()
    time.sleep(3)
    """

    username = driver.find_element(By.ID, 'username')
    email = driver.find_element(By.ID, 'email')
    username.send_keys('hyethanh')
    action.key_down(Keys.CONTROL).key_down('A').perform()
    time.sleep(2)
    action.key_down(Keys.CONTROL).key_down('C').perform()
    time.sleep(2)
    action.click(email).key_down(Keys.CONTROL).key_down('V').perform()
    time.sleep(2)

    driver.quit()
