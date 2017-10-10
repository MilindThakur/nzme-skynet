# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.enums.drivertypes import DESKTOP_WEBBROWSER, DriverTypes, MOBILE_WEBBROWSER, MOBILE_APP
from nzme_skynet.core.driver.driverfactory import DriverFactory
from nzme_skynet.core.driver import register_driver, deregister_driver, get_driver


class DriverRegistry(object):
    """
    Responsible for calling DriverFactory to build driver and registering driver to be used in tests.
    The driver is registered at a global level. Currently supports registration
    of only one driver at any time.
    """

    @staticmethod
    def register_driver(driver_type='chrome', driver_options=None, local=True):
        new_driver = None
        try:
            if driver_type in DESKTOP_WEBBROWSER:
                if local:
                    new_driver = DriverFactory.build_local_web_driver(driver_type, driver_options)
                else:
                    new_driver = DriverFactory.build_remote_web_driver(driver_type, driver_options)
            elif driver_type in MOBILE_WEBBROWSER:
                new_driver = DriverFactory.build_mobile_web_driver(driver_type, driver_options,
                                                                   browser=DriverTypes.CHROME)
            elif driver_type in MOBILE_APP:
                new_driver = DriverFactory.build_mobile_app_driver(driver_type, driver_options)
            register_driver(new_driver)
        except Exception:
            raise

    @staticmethod
    def deregister_driver():
        if not get_driver():
            raise Exception("No registered driver found")
        get_driver().quit()
        deregister_driver()

    @staticmethod
    def get_driver():
        if not get_driver():
            raise Exception("No registered driver found")
        return get_driver()
