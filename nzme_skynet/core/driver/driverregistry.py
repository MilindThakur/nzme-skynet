# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.basedriver import BaseDriver
from nzme_skynet.core.driver.enums.drivertypes import DESKTOP_WEBBROWSER, DriverTypes, MOBILE_WEBBROWSER, MOBILE_APP
from nzme_skynet.core.driver.driverfactory import DriverFactory
from nzme_skynet.core.controls import set_highlight, highlight_state
from nzme_skynet.core.driver import register_driver, deregister_driver, get_driver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.phantomjs.webdriver import WebDriver
import signal
import logging
from nzme_skynet.core.utils.log import Logger


Logger.configure_logging()
logger = logging.getLogger(__name__)


class DriverRegistry(object):
    """
    Responsible for calling DriverFactory to build driver and registering driver to be used in tests.
    The driver is registered at a global level. Currently supports registration
    of only one driver at any time.
    """

    @staticmethod
    def register_driver(driver_type='chrome', capabilities=None, local=True, grid_url="http://127.0.0.1:4444/wd/hub"):
        """
        Build and register driver
        :param driver_type: DriverTypes
        :param capabilities: capabilities
        :param local: Local or Selenium Grid/Server
        :param grid_url: Selenium grid url
        :return:
        """
        new_driver = None
        if get_driver():
            logger.warning("Driver already registered. Only one driver can be registered at a time")
            return get_driver()
        set_highlight(capabilities['highlight'] if capabilities and 'highlight' in capabilities else False)
        try:
            if local:
                if driver_type in DESKTOP_WEBBROWSER:
                    new_driver = DriverFactory.build_local_web_driver(driver_type, capabilities)
                elif driver_type in MOBILE_WEBBROWSER:
                    new_driver = DriverFactory.build_mobile_web_driver(driver_type, capabilities, grid_url)
                elif driver_type in MOBILE_APP:
                    new_driver = DriverFactory.build_mobile_app_driver(driver_type, capabilities, grid_url)
            else:
                new_driver = DriverFactory.build_remote_web_driver(capabilities, grid_url)
            register_driver(new_driver)
            return get_driver()
        except Exception as e:
            logger.exception("Failed to register driver")
            raise

    @staticmethod
    def deregister_driver():
        """
        Removes current driver from registry
        :return:
        """
        if get_driver():
            # https://github.com/seleniumhq/selenium/issues/767
            if isinstance(DriverRegistry.get_webdriver(), WebDriver):
                DriverRegistry.get_webdriver().service.process.send_signal(signal.SIGTERM)
            DriverRegistry.get_webdriver().quit()
            deregister_driver()
            logger.debug("Successfully deregistered driver")
            set_highlight(False)

    @staticmethod
    def get_driver():
        # type: () -> BaseDriver
        """
        Returns Skynet driver from registry
        """
        return get_driver()

    @staticmethod
    def get_webdriver():
        # type: () -> [WebDriver, None]
        """
        Returns Selenium Webdriver from registry
        :return:
        """
        if get_driver():
            return get_driver().webdriver
        logger.error("No registered driver found")
        return None
