# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes
from nzme_skynet.core.driver.mobile.appiumdriver import AppiumDriver
from appium import webdriver


class MApp(AppiumDriver):

    def __init__(self, mplatform, desired_capabilities, appium_server_url='http://127.0.0.1:4444/wd/hub'):
        self._mplatform = mplatform
        self._appium_server_url = appium_server_url
        self._desired_capabilities = desired_capabilities

    def _set_default_capability(self):
        self._create_desired_capabilities()
        self._desired_capabilities['fullReset'] = 'True'
        self._desired_capabilities['clearSystemFiles'] = 'True'

    def _create_desired_capabilities(self):
        if not self._desired_capabilities:
            raise Exception("No capabilities provided to init Appium driver")
        if not self._desired_capabilities['platformVersion']:
            raise Exception("Please provide platformVersion to test app against")
        if not self._desired_capabilities['app']:
            raise Exception("Please provide absolute app path")
        if self._mplatform == DriverTypes.ANDROID:
            if not self._desired_capabilities['appPackage']:
                raise Exception("Please provide the java package of the app")
            if not self._desired_capabilities['appActivity']:
                raise Exception("Please provide the activity to launch")
            self._desired_capabilities['platformName'] = 'Android'
            self._desired_capabilities['platform'] = 'ANDROID'
            if not self._desired_capabilities['deviceName']:
                # Run tests on Android emulator by default
                self._desired_capabilities['deviceName'] = 'Android Emulator'
        if self._mplatform == DriverTypes.IOS:
            raise NotImplementedError

    def add_capability(self, name, value):
        self._desired_capabilities[name] = value

    def create_driver(self):
        self._set_default_capability()
        return webdriver.Remote(command_executor=self._appium_server_url,
                                desired_capabilities=self._desired_capabilities)
