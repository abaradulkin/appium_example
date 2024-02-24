from pytest import *
from common.constant import Platforms


def pytest_addoption(parser):
    parser.addoption(
        '--platform', action='store', default=Platforms.ANDROID, help='Platform for test running')
    parser.addoption('--device', action='store', default='Pixel 7 API 34',
                     help='Device name for test on emulator or real device. Left empty for Web testing')


@fixture(scope="session")
def device_name(request):
    return request.config.getoption('--device')


@fixture(scope="session")
def platform(request):
    return request.config.getoption('--platform')


@fixture(scope="session")
def appium_default_capabilities(platform, device_name):
    capabilities = dict(
        platformName=platform.value,
        deviceName=device_name,
        appPackage='com.playrix.manormatters',
        appActivity='.GoogleGameActivity',
        language='en',
        locale='US',
        noReset=False
    )

    if platform == Platforms.ANDROID:
        capabilities["automationName"] = "uiautomator2"
    elif platform == Platforms.IOS:
        capabilities["automationName"] = "xcuitest"
    else:
        raise Exception(platform, "still not implemented!")

    yield capabilities
