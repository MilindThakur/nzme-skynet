# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.mobile.browser.mbrowserdriver import MBrowserDriver
import logging
logger = logging.getLogger(__name__)

class IOSBrowserDriver(MBrowserDriver):

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
        logger.debug("iOS capability for creating driver {0}".format(self._desired_cap))
