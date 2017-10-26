# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.mobile.browser.mbrowserdriver import MBrowserDriver


class IOSBrowserDriver(MBrowserDriver):

    def __init__(self, desired_capabilities, browsername="Safari", remote_url='http://127.0.0.1:4444/wd/hub'):
        super(IOSBrowserDriver, self).__init__(desired_capabilities, browsername, remote_url)

    def _create_desired_capabilities(self):
        if not self._desired_cap:
            raise Exception("No capabilities provided to init Appium driver")
        if not self._desired_cap['platformVersion']:
            raise Exception("Please provide platformVersion to test app against")
        if self._browser not in ['Safari', 'Chrome']:
            raise Exception("Only supports Safari and Chrome browsers on IOS")

        self._desired_cap['browserName'] = self._browser
        self._desired_cap['platformName'] = 'iOS'
        self._desired_cap['platform'] = 'iOS'
        if not self._desired_cap['deviceName']:
            # Run tests on Android emulator by default
            self._desired_cap['deviceName'] = 'iPhone Simulator'
