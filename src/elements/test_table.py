import time

from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_table():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/webtable/")
    assert 'webtable' in driver.title

    table = driver.find_element(By.ID, 'table01')
    # headers = table.find_elements(By.TAG_NAME, 'th')
    table_body = table.find_element(By.TAG_NAME, 'tbody')
    rows = table_body.find_elements(By.TAG_NAME, 'tr')
    cells = table_body.find_elements(By.TAG_NAME, 'td')

    print(len(rows))

    for i in range(len(rows)):
        columns = rows[i].find_elements(By.TAG_NAME, 'td')
        for j in range(len(columns)):
            if columns[j].text == 'TFS':
                columns[0].click()

    time.sleep(3)
    driver.save_screenshot("screen/screenshot.png")

    """
    for cell in cells:
        print(cell.text)
    """
    driver.quit()
