# coding=utf-8
from nzme_skynet.core.driver.mobile.app.mappdriver import MAppDriver
from appium.webdriver.webdriver import WebDriver


class IOSAppDriver(MAppDriver):

    def __init__(self, desired_capabilities, remote_url='http://127.0.0.1:4444/wd/hub'):
        self._desired_cap = desired_capabilities
        self._remote_url = remote_url
        self._driver = None

    def _create_driver(self):
        self._driver = WebDriver(command_executor=self._remote_url, desired_capabilities=self._desired_cap)

    def _set_default_capabilities(self):
        self._create_desired_capabilities()
        self._desired_cap['fullReset'] = 'True'

    def _create_desired_capabilities(self):
        if not self._desired_cap:
            raise Exception("No capabilities provided to init Appium driver")
        if not self._desired_cap['platformVersion']:
            raise Exception("Please provide platformVersion to test app against")
        if not self._desired_cap['bundleId']:
            raise Exception("Please provide bundle ID")
        if not self._desired_cap['app']:
            raise Exception("Please provide absolute app path for .ipa")
        if not self._desired_cap['appActivity']:
            raise Exception("Please provide the activity to launch")

        self._desired_cap['platformName'] = 'iOS'
        self._desired_cap['platform'] = 'iOS'
        if not self._desired_cap['deviceName']:
            # Run tests on Android emulator by default
            self._desired_cap['deviceName'] = 'iPhone Simulator'
        if not self._desired_cap['automation']:
            self._desired_cap['automation'] = 'XCUITest'

    @property
    def webdriver(self):
        # type: () -> WebDriver
        return self._driver
