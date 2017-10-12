# -*- coding: utf-8 -*-

from nzme_skynet.core.driver.enums.drivertypes import DriverTypes
from nzme_skynet.core.driver.mobile.app.androidappdriver import AndroidAppDriver
from nzme_skynet.core.driver.mobile.app.iosappdriver import IOSAppDriver
from nzme_skynet.core.driver.mobile.browser.androidbrowserdriver import AndroidBrowserDriver
from nzme_skynet.core.driver.mobile.browser.iosbrowserdriver import IOSBrowserDriver
from nzme_skynet.core.driver.web.browsers.chrome import Chrome
from nzme_skynet.core.driver.web.browsers.firefox import FireFox
from nzme_skynet.core.driver.web.browsers.phantomjs import PhantomJS
from nzme_skynet.core.driver.web.browsers.remote import Remote


class DriverFactory(object):
    """
    A simple driver factory that creates and returns driver based on browser/app
    type and test environment (local/grid).
    """

    @staticmethod
    def build_local_web_driver(driver_type="chrome", driver_options=None):
        if driver_type == DriverTypes.CHROME:
            driver = Chrome(driver_options)
        elif driver_type == DriverTypes.FIREFOX:
            driver = FireFox(driver_options)
        elif driver_type == DriverTypes.PHANTOMJS:
            driver = PhantomJS(driver_options)
        else:
            raise Exception("Only supports Chrome, Firefox, PhantomJS in local mode")
        try:
            driver.init()
            return driver
        except Exception:
            raise Exception("Failed to initialise local web driver")

    @staticmethod
    def build_mobile_app_driver(driver_type, driver_capabilities):
        if driver_type == DriverTypes.IOS:
            driver = IOSAppDriver(desired_capabilities=driver_capabilities)
        elif driver_type == DriverTypes.ANDROID:
            driver = AndroidAppDriver(desired_capabilities=driver_capabilities)
        else:
            raise Exception("Only supports Android and IOS app drivers")
        try:
            driver.init()
            return driver
        except Exception:
            raise Exception("Failed to initialise mobile app driver")

    @staticmethod
    def build_mobile_web_driver(driver_type, driver_capabilities, browsername):
        if driver_type == DriverTypes.IOSWEB:
            driver = IOSBrowserDriver(desired_capabilities=driver_capabilities, browsername=browsername)
        elif driver_type == DriverTypes.ANDROIDWEB:
            driver = AndroidBrowserDriver(desired_capabilities=driver_capabilities, browsername=browsername)
        else:
            raise Exception("Only supports Android and IOS browser drivers")

        try:
            driver.init()
            return driver
        except Exception:
            raise Exception("Failed to initialise mobile browser driver")

    @staticmethod
    def build_remote_web_driver(driver_type="chrome", driver_options=None):
        if not driver_options:
            if driver_type == DriverTypes.CHROME:
                driver_options = Chrome.get_default_capability()
            elif driver_type == DriverTypes.FIREFOX:
                driver_options = FireFox.get_default_capability()
            else:
                raise Exception("Only supports Chrome and Firefox in remote mode when no capabilities passed")
        driver = Remote(driver_options)
        try:
            return driver.init()
        except Exception:
            raise Exception("Failed to initialise remote web driver")
