# coding=utf-8
from nzme_skynet.core.browsers.web.browserTypes import BrowserTypes
from nzme_skynet.core.browsers.mobile.androidDriver import AndroidDriver
from nzme_skynet.core.browsers.mobile.iosDriver import IosDriver


class AppiumDriverBuilder(object):
    def __init__(self, desired_caps):
        self.desired_caps = desired_caps
        self._driverType = desired_caps.get('type')

    def build(self):
        driver = self._construct_driver()
        driver.init_driver()
        return driver

    def _construct_driver(self):
        try:
            if self._driverType == BrowserTypes.ANDROID:
                return AndroidDriver(self.desired_caps)
            if self._driverType == BrowserTypes.IOS:
                return IosDriver(self.desired_caps)
                # return AndroidDriver(self.desired_caps)
                raise NotImplementedError
            # TODO - this will need to be implemented at some stage
            if (self._driverType == BrowserTypes.ANDROID_BROWSER) or (self._browserType == BrowserTypes.IOS_BROWSER):
                raise NotImplementedError
            else:
                raise ValueError("only Android, iOS, Android browser and iOS browser are supported")
        except Exception, E:
            raise StandardError("Failed constructing appium driver." + E.message)
