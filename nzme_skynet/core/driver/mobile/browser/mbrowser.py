# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes
from nzme_skynet.core.driver.mobile.appiumdriver import AppiumDriver
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class MBrowser(AppiumDriver):

    def __init__(self, platform, appium_server_url='http://127.0.0.1:4444/wd/hub', desired_capabilities=None,
                 browser=None):
        self._platform = platform
        self._appium_server_url = appium_server_url
        self._desired_capabilities = desired_capabilities
        self._browser = browser

    def _set_default_capabilities(self):
        if not self._browser:
            self._browser = DriverTypes.CHROME
        self._create_desired_capabilities()
        self._set_browser_capability(self._browser)

    def _create_desired_capabilities(self):
        if not self._desired_capabilities:
            if self._platform == DriverTypes.ANDROID:
                self._desired_capabilities = DesiredCapabilities.ANDROID.copy()
                self._desired_capabilities['deviceName'] = 'Android Emulator'
            if self._platform == DriverTypes.IOS:
                # TODO: add more ios capabilities
                self._desired_capabilities = DesiredCapabilities.IPHONE.copy()

    def _set_browser_capability(self, browsername):
        self._desired_capabilities['browserName'] = browsername
        if browsername == DriverTypes.CHROME:
            self._desired_capabilities['chromeOptions'] = {'args': '--no-first-run'}

    def add_capability(self, name, value):
        self._desired_capabilities[name] = value

    def create_driver(self):
        self._set_default_capabilities()
        return webdriver.Remote(command_executor=self._appium_server_url,
                                desired_capabilities=self._desired_capabilities)
