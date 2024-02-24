from pytest import *
from allure import attach, attachment_type
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene.support.shared import browser, config


@fixture(autouse=True, scope="class")
def driver_fixture(appium_default_capabilities, platform):
    appium_server_url = 'http://localhost:4723'

    try:
        config.driver = webdriver.Remote(appium_server_url,
                                         options=UiAutomator2Options().load_capabilities(appium_default_capabilities))
        config.platform = platform

        config.timeout = 10

        yield config.driver
    finally:
        config.driver.quit()


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        attach(browser.driver.get_screenshot_as_png(), name="Screenshot.jpeg", attachment_type=attachment_type.PNG)
