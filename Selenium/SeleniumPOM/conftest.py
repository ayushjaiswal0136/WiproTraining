import time

import pytest
from selenium import webdriver


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.amazon.in")
    time.sleep(3)
    yield driver
    driver.quit()

