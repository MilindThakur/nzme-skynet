# coding=utf-8
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes
from nzme_skynet.core.driver.mobile.app.androiddriver import AndroidDriver
from nzme_skynet.core.driver.mobile.browser.mobilebrowser import MobileBrowser


class AppiumDriverBuilder(object):

    def __init__(self, desired_caps):
        self._desired_caps = desired_caps
        self.driver = None

    def build(self):
        driver = self._construct_driver()
        driver.init_driver()
        return driver

    def _construct_driver(self):
        try:
            if 'browserName' in self._desired_caps:
                return MobileBrowser(self._desired_caps)
            if self._desired_caps['platform'].lower() == DriverTypes.ANDROID:
                return AndroidDriver(self._desired_caps)
            if self._desired_caps['platform'].lower() == DriverTypes.IOS:
                raise NotImplementedError
                # return IosDriver(self.desired_caps)
            # TODO - this will need to be implemented at some stage
            else:
                raise ValueError("only Android, Android browser are supported")
        except Exception, E:
            raise StandardError("Failed constructing appium driver." + E.message)
