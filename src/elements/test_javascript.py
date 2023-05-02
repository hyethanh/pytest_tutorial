import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_javascript():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/signup/")
    driver.implicitly_wait(38)
    driver.set_page_load_timeout(58)
    assert 'Registration' in driver.title
    #
    # print('Title = ' + driver.execute_script('return document.title'))
    # print('URL = ' + driver.execute_script('return document.URL'))
    # print('Is Page Loaded: ' + driver.execute_script('return document.readyState'))

    """
    # using javascript to indentify and click element
    driver.execute_script("window.location = 'https://qavbox.github.io/demo/'")
    element = driver.execute_script("return document.querySelector(\"[href='/demo/signup']\")")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)
    """

    """
    driver.execute_script("return document.getElementById('username').value='hyethanh'")
    print('Entered value is: ' + driver.execute_script("return document.getElementById('username').value"))
    """

    driver.execute_script("return window.scrollTo(0, document.body.scrollHeight)")
    driver.execute_script("return document.querySelector('input[value=\"seven\"]').checked=true")
    time.sleep(2)

    driver.quit()
