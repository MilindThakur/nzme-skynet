# coding=utf-8
from nzme_skynet.core.driver.mobile.app.mappdriver import MAppDriver
from appium.webdriver.webdriver import WebDriver


class AndroidAppDriver(MAppDriver):

    def __init__(self, desired_capabilities, remote_url='http://127.0.0.1:4444/wd/hub'):
        self._desired_cap = desired_capabilities
        self._remote_url = remote_url
        self._driver = None

    def _create_driver(self):
        self._driver = WebDriver(command_executor=self._remote_url, desired_capabilities=self._desired_cap)

    @property
    def webdriver(self):
        # type: () -> WebDriver
        return self._driver
