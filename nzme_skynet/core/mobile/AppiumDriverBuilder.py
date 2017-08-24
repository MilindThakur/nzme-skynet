# coding=utf-8
from nzme_skynet.core.mobile.drivers.androidDriver import AndroidDriver
from nzme_skynet.core.mobile.drivers.mobilebrowser import Mobilebrowser
from nzme_skynet.core.mobile.enums.drivertypes import DriverTypes
from nzme_skynet.core.mobile.drivers.iosDriver import IosDriver


class AppiumDriverBuilder(object):
    def __init__(self, desired_caps):
        self.desired_caps = desired_caps
        self._driverType = desired_caps.get('platform').lower()
        self.driver = None

    def build(self):
        driver = self._construct_driver()
        driver.init_driver()
        return driver

    def _construct_driver(self):
        try:
            if self.desired_caps['browserName'] is not None:
                return Mobilebrowser(self.desired_caps)
            if self._driverType == DriverTypes.ANDROID:
                return AndroidDriver(self.desired_caps)
            if self._driverType == DriverTypes.IOS:
                return IosDriver(self.desired_caps)
                # return IOSDriver(self.desired_caps)
                raise NotImplementedError
            # TODO - this will need to be implemented at some stage
            else:
                raise ValueError("only Android, iOS, Android browser and iOS browser are supported")
        except Exception, E:
            raise StandardError("Failed constructing appium driver." + E.message)
