# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.basedriver import BaseDriver
from nzme_skynet.core.driver.enums.drivertypes import DESKTOP_WEBBROWSER, MOBILE_WEBBROWSER, MOBILE_APP
from nzme_skynet.core.driver.driverfactory import DriverFactory
from nzme_skynet.core.driver import register_driver, deregister_driver, get_driver
from selenium.webdriver.remote.webdriver import WebDriver
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
    def register_driver(driver_type='chrome', capabilities=None, local=True, grid_url="http://127.0.0.1:4444/wd/hub", options=None):
        """
        Build and register driver
        :param driver_type: DriverTypes
        :param capabilities: capabilities
        :param local: Local or Selenium Grid/Server
        :param grid_url: Selenium grid url
        :return:
        """
        if get_driver():
            logger.warning(
                "Driver already registered. Only one driver can be registered at a time")
            return get_driver()
        try:
            if driver_type in DESKTOP_WEBBROWSER:
                new_driver = DriverFactory.build_web_driver(
                    driver_type, capabilities, options, local, grid_url)
            elif driver_type in MOBILE_WEBBROWSER:
                new_driver = DriverFactory.build_mobile_web_driver(
                    driver_type, capabilities, grid_url)
            elif driver_type in MOBILE_APP:
                new_driver = DriverFactory.build_mobile_app_driver(
                    driver_type, capabilities, grid_url)
            else:
                logger.exception(
                    "Empty or Unknown driver type, valid options: chrome, firefox, safari, ie, android, ios")
                raise Exception(
                    "Empty or Unknown driver type, valid options: chrome, firefox, safari, ie, android, ios")
        except Exception:
            logger.exception("Failed to register driver")
            raise
        register_driver(new_driver)
        return get_driver()

    @staticmethod
    def deregister_driver():
        """
        Removes current driver from registry
        :return:
        """
        if get_driver():
            DriverRegistry.get_webdriver().quit()
            deregister_driver()
            logger.debug("Successfully deregistered driver")

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
