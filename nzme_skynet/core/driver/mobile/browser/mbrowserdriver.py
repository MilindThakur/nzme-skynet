# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.mobile.mobiledriver import MobileDriver
from nzme_skynet.core.driver.web.browserdriver import BrowserDriver
from appium.webdriver.webdriver import WebDriver


class MBrowserDriver(MobileDriver, BrowserDriver):

    def __init__(self, desired_capabilities, browsername="Safari", remote_url='http://127.0.0.1:4444/wd/hub'):
        self._desired_cap = desired_capabilities
        self._browser = browsername
        self._remote_url = remote_url
        self._driver = None

    def _create_driver(self):
        self._set_default_capabilities()
        self._driver = WebDriver(command_executor=self._remote_url, desired_capabilities=self._desired_cap)

    def _set_default_capabilities(self):
        self._create_desired_capabilities()
        self._desired_cap['fullReset'] = 'True'

    def _create_desired_capabilities(self):
       raise NotImplementedError

    @property
    def webdriver(self):
        # type: () -> WebDriver
        return self._driver

    def init(self):
        self._create_driver()
