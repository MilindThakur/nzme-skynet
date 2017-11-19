# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.basedriver import BaseDriver
from nzme_skynet.core.driver.enums.drivertypes import DESKTOP_WEBBROWSER, DriverTypes, MOBILE_WEBBROWSER, MOBILE_APP
from nzme_skynet.core.driver.driverfactory import DriverFactory
from nzme_skynet.core.driver import register_driver, deregister_driver, get_driver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.phantomjs.webdriver import WebDriver
import signal


class DriverRegistry(object):
    """
    Responsible for calling DriverFactory to build driver and registering driver to be used in tests.
    The driver is registered at a global level. Currently supports registration
    of only one driver at any time.
    """

    @staticmethod
    def register_driver(driver_type='chrome', driver_options=None, local=True, mbrowsername=DriverTypes.CHROME,
                        grid_url="http://127.0.0.1:4444/wd/hub"):
        """
        Build and register driver
        :param driver_type: DriverTypes
        :param driver_options: capabilities
        :param local: Local or Selenium Grid/Server
        :param mbrowsername: mobile browser type, default chrome
        :param grid_url: Selenium grid url
        :return:
        """
        new_driver = None
        if get_driver():
            raise Exception("Only one driver can be registered at a time")
        try:
            if driver_type in DESKTOP_WEBBROWSER:
                if local:
                    new_driver = DriverFactory.build_local_web_driver(driver_type, driver_options)
                else:
                    new_driver = DriverFactory.build_remote_web_driver(driver_type, driver_options, grid_url)
            elif driver_type in MOBILE_WEBBROWSER:
                new_driver = DriverFactory.build_mobile_web_driver(driver_type, driver_options,
                                                                   browsername=mbrowsername)
            elif driver_type in MOBILE_APP:
                new_driver = DriverFactory.build_mobile_app_driver(driver_type, driver_options)
            register_driver(new_driver)
            return get_driver()
        except Exception:
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

    @staticmethod
    def get_driver():
        # type: () -> BaseDriver
        """
        Returns Skynet driver from registry
        """
        return get_driver()

    @staticmethod
    def get_webdriver():
        # type: () -> WebDriver
        """
        Returns Selenium Webdriver from registry
        :return:
        """
        if not get_driver():
            raise Exception("No registered driver found")
        return get_driver().webdriver

