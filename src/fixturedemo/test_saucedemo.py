import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from src.fixturedemo.base_test import BaseTest


# @pytest.mark.usefixtures("get_driver")
class TestSauceDemo2(BaseTest):

    def test_saucedemo(self):
        driver = self.driver

        driver.find_element(By.ID, 'user-name').send_keys('standard_user')
        driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        driver.find_element(By.ID, 'login-button').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'inventory_container')))



