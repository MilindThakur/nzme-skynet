# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes
from nzme_skynet.core.driver.mobile.app.androidappdriver import AndroidAppDriver
from nzme_skynet.core.driver.mobile.app.iosappdriver import IOSAppDriver
from nzme_skynet.core.driver.mobile.browser.androidbrowserdriver import AndroidBrowserDriver
from nzme_skynet.core.driver.mobile.browser.iosbrowserdriver import IOSBrowserDriver
from nzme_skynet.core.driver.web.browsers.chrome import Chrome
from nzme_skynet.core.driver.web.browsers.edge import Edge
from nzme_skynet.core.driver.web.browsers.firefox import Firefox
from nzme_skynet.core.driver.web.browsers.ie import IE
from nzme_skynet.core.driver.web.browsers.safari import Safari
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
from nzme_skynet.core.utils.log import Logger

Logger.configure_logging()
logger = logging.getLogger(__name__)


class DriverFactory(object):
    """
    A simple driver factory that creates and returns driver based on browser/app
    type and test environment (local/grid).
    """

    @staticmethod
    def build_web_driver(driver_type, capabilities, options, local, grid_url):
        if driver_type == "chrome":
            driver = Chrome(capabilities, options)
        elif driver_type == "firefox":
            driver = Firefox(capabilities, options)
        elif driver_type == "safari":
            driver = Safari(capabilities, options)
        elif driver_type == "edge":
            driver = Edge(capabilities, options)
        elif driver_type == "ie":
            driver = IE(capabilities, options)
        else:
            logger.exception(
                "Only supports Chrome, Firefox, Safari, Edge, IE in browser mode")
            raise Exception(
                "Only supports  Chrome, Firefox, Safari, Edge, IE in browser mode")
        try:
            driver.init(local, grid_url)
            logger.debug(
                "Successfully initialised web driver {0}".format(driver_type))
            return driver
        except Exception as e:
            logger.exception("Failed to initialise local web driver")
            raise

    @staticmethod
    def build_mobile_app_driver(driver_type, capabilities, remote_url):
        if driver_type == DriverTypes.IOS:
            driver = IOSAppDriver(
                desired_capabilities=capabilities, remote_url=remote_url)
        elif driver_type == DriverTypes.ANDROID:
            driver = AndroidAppDriver(
                desired_capabilities=capabilities, remote_url=remote_url)
        else:
            logger.exception("Only supports Android and IOS app drivers")
            raise Exception("Only supports Android and IOS app drivers")
        try:
            driver.init()
            logger.debug(
                "Successfully initialised mobile app driver {0}".format(driver_type))
            return driver
        except Exception as e:
            logger.exception("Failed to initialise mobile app driver")
            raise

    @staticmethod
    def build_mobile_web_driver(driver_type, capabilities, remote_url):
        if driver_type == DriverTypes.IOSWEB:
            driver = IOSBrowserDriver(
                desired_capabilities=capabilities, remote_url=remote_url)
        elif driver_type == DriverTypes.ANDROIDWEB:
            driver = AndroidBrowserDriver(
                desired_capabilities=capabilities, remote_url=remote_url)
        else:
            logger.exception("Only supports Android and IOS browser drivers")
            raise Exception("Only supports Android and IOS browser drivers")
        try:
            driver.init()
            logger.debug("Successfully initialised mobile web driver")
            return driver
        except Exception as e:
            logger.exception("Failed to initialise mobile browser driver")
            raise
