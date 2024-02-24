from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from base64 import b64encode
from os.path import relpath
from selene import by, be, have, query
from selene.support.shared import config
from selene.support.shared.jquery_style import s, ss, Element, Collection


def _locator_from_platform(locators_dict: dict) -> tuple:
    locator_type, locator = locators_dict.get(config.platform, locators_dict.get("default"))
    if locator_type == AppiumBy.IMAGE:
        with open(relpath(locator), "rb") as image_file:
            locator = b64encode(image_file.read()).decode("utf-8")
    return locator_type, locator


def element(locator: dict) -> Element:
    return s(_locator_from_platform(locator))


def elements(locator: dict) -> Collection:
    return ss(_locator_from_platform(locator))
