from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_sample_dropdown():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://qavbox.github.io/demo/signup/")
    assert 'Registration' in driver.title
    select = Select(driver.find_element(By.NAME, 'sgender'))
    # select.select_by_value("female")
    # select.select_by_visible_text('Male')
    select.select_by_index(3)       #index starts 0
    print("\nSelected item: {}".format(select.first_selected_option.text))
    assert 'Not Applicable' in select.first_selected_option.text

    opts = select.options
    print("Dropdown options are:\n")
    for opt in opts:
        print(opt.text)
    driver.quit()
