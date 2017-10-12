# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.mobile.browser.mbrowserdriver import MBrowserDriver


class AndroidBrowserDriver(MBrowserDriver):

    def __init__(self, desired_capabilities, browsername="Chromium", remote_url='http://127.0.0.1:4444/wd/hub'):
        super(AndroidBrowserDriver, self).__init__(desired_capabilities, browsername, remote_url)

    def _create_desired_capabilities(self):
        if not self._desired_cap:
            raise Exception("No capabilities provided to init Appium driver")
        if not self._desired_cap['platformVersion']:
            raise Exception("Please provide platformVersion to test app against")
        if self._browser not in ['Chrome', 'Browser']:
            raise Exception("Only supports Chrome and native Browser on Android")

        self._desired_cap['browserName'] = self._browser
        self._desired_cap['platformName'] = 'Android'
        self._desired_cap['platform'] = 'ANDROID'
        if not self._desired_cap['deviceName']:
            # Run tests on Android emulator by default
            self._desired_cap['deviceName'] = 'Android Emulator'
