import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from src.fixturedemo import settings


# browser = 'chrome'


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=settings.browser)


@pytest.fixture
def get_browser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture
def get_driver(request, get_browser):
    _driver = None
    if get_browser == 'chrome':
        _driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif get_browser == 'firefox':
        _driver = webdriver.Firefox()

    _driver.maximize_window()
    _driver.get("https://www.saucedemo.com")
    _driver.implicitly_wait(20)
    request.cls.driver = _driver
    yield request.cls.driver
    time.sleep(2)
    request.cls.driver.quit()
