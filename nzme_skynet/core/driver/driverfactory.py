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
    def build_local_web_driver(browser=DriverTypes.CHROME, capabilities=None):
        if browser == DriverTypes.CHROME:
            driver = Chrome(capabilities)
        elif browser == DriverTypes.CHROMEHEADLESS:
            driver = Chrome(capabilities, headless=True)
        elif browser == DriverTypes.FIREFOX:
            driver = FireFox(capabilities)
        elif browser == DriverTypes.PHANTOMJS:
            driver = PhantomJS(capabilities)
        else:
            logger.exception("Only supports Chrome, Firefox, PhantomJS in local mode")
            raise Exception("Only supports Chrome, Firefox, PhantomJS in local mode")
        try:
            driver.init()
            logger.debug("Successfully initialised local web driver {0}".format(browser))
            return driver
        except Exception as e:
            logger.exception("Failed to initialise local web driver")
            raise

    @staticmethod
    def build_mobile_app_driver(driver_type, capabilities, remote_url):
        if driver_type == DriverTypes.IOS:
            driver = IOSAppDriver(desired_capabilities=capabilities, remote_url=remote_url)
        elif driver_type == DriverTypes.ANDROID:
            driver = AndroidAppDriver(desired_capabilities=capabilities, remote_url=remote_url)
        else:
            logger.exception("Only supports Android and IOS app drivers")
            raise Exception("Only supports Android and IOS app drivers")
        try:
            driver.init()
            logger.debug("Successfully initialised mobile app driver {0}".format(driver_type))
            return driver
        except Exception as e:
            logger.exception("Failed to initialise mobile app driver")
            raise

    @staticmethod
    def build_mobile_web_driver(driver_type, capabilities, remote_url):
        if driver_type == DriverTypes.IOSWEB:
            driver = IOSBrowserDriver(desired_capabilities=capabilities, remote_url=remote_url)
        elif driver_type == DriverTypes.ANDROIDWEB:
            driver = AndroidBrowserDriver(desired_capabilities=capabilities, remote_url=remote_url)
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

    @staticmethod
    def build_remote_web_driver(capabilities=None, grid_url="http://127.0.0.1:4444/wd/hub"):
        if not capabilities:
            capabilities = Chrome.get_default_capability()
            logger.warning("No capabilities specified, using chrome as default remote browser")
        driver = Remote(capabilities, remote_url=grid_url)
        try:
            driver.init()
            logger.debug("Successfully initialised remote web driver".format(capabilities['browserName']))
            return driver
        except Exception as e:
            logger.exception("Failed to initialise remote web driver")
            raise
