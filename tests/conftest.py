import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True, scope='session')
def browser_management():
    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    webdriver.ChromeOptions()

    yield

    browser.quit()
