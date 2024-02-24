from common.constant import Platforms
from ui.element import *

welcome_logo = {"default": (AppiumBy.IMAGE, "ui/first_page/welcome_logo.png")}
start_button = {"default": (AppiumBy.IMAGE, "ui/first_page/skip.png")}
introducing_text = {Platforms.ANDROID: (AppiumBy.IMAGE, "ui/first_page/introduction_android.png"),
                    Platforms.IOS: (AppiumBy.IMAGE, "ui/first_page/introduction_ios.png")}


@step("Click on skip button")
def click_skip_button():
    element(start_button).click()


@step("Check first quest loaded")
def is_first_quest_dialog():
    return element(introducing_text).wait_until(be.visible)


@step("Wait till game be loaded")
def wait_game_loaded():
    return element(welcome_logo).wait_until(be.hidden)
