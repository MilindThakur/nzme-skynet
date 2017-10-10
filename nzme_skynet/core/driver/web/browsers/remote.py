# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver

from nzme_skynet.core.driver.web.browserdriver import BrowserDriver


class Remote(BrowserDriver):

    def __init__(self, desired_cap, remote_url='http://127.0.0.1:4444/wd/hub'):
        self._desired_cap = desired_cap
        self._remote_url = remote_url
        self._driver = None

    def add_option(self, option):
        pass

    def add_extension(self, extension):
        pass

    def _create_driver(self):
        self._driver = WebDriver(command_executor=self._remote_url, desired_capabilities=self._desired_cap)

    def get_webdriver(self):
        # type: () -> WebDriver
        if not self._driver:
            raise Exception("Driver has not been created")
        return self._driver
