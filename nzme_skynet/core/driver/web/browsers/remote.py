# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.web.browsers.browserdriver import BrowserDriver
from selenium.webdriver.remote.webdriver import WebDriver


class Remote(BrowserDriver):

    def __init__(self, desired_cap, remote_url='http://127.0.0.1:4444/wd/hub'):
        self._desired_cap = desired_cap
        self._remote_url = remote_url

    def add_option(self, option):
        pass

    def add_extension(self, extension):
        pass

    def create_driver(self):
        return WebDriver(command_executor=self._remote_url, desired_capabilities=self._desired_cap)
