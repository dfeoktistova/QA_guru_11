import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach


@pytest.fixture(autouse=True, scope='function')
def browser_management():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
