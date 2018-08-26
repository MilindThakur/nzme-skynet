# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.mobile.browser.mbrowserdriver import MBrowserDriver
import logging
logger = logging.getLogger(__name__)

class AndroidBrowserDriver(MBrowserDriver):

    def _create_desired_capabilities(self):
        if not self._desired_cap:
            raise Exception("No capabilities provided to init Appium driver")
        if not self._desired_cap['version']:
            raise Exception("Please provide platformVersion to test app against")
        if self._browser not in ['chrome', 'Browser']:
            raise Exception("Only supports Chrome and native Browser on Android")

        if "chrome" in self._desired_cap['browserName']:
            # To disable the welcome screen on launching chrome
            self.add_chrome_options('--no-first-run')
        self._desired_cap['platformName'] = 'Android'
        self._desired_cap['platform'] = 'ANDROID'
        if not self._desired_cap['deviceName']:
            # Run tests on Android emulator by default
            self._desired_cap['deviceName'] = 'Android Emulator'
        logger.debug("Android capability for creating driver: {0}".format(self._desired_cap))

    def add_chrome_options(self, option):
        if "chromeOptions" in self._desired_cap:
            self._desired_cap['chromeOptions']['args'].append(option)
        else:
            self._desired_cap['chromeOptions'] = {'args': [option]}
