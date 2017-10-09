# -*- coding: utf-8 -*-

from nzme_skynet.core.driver.enums.drivertypes import DESKTOP_WEBDRIVERS
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes
from nzme_skynet.core.driver.mobile.app.mapp import MApp
from nzme_skynet.core.driver.mobile.browser.mbrowser import MBrowser
from nzme_skynet.core.driver.web.browsers.chrome import Chrome
from nzme_skynet.core.driver.web.browsers.firefox import FireFox
from nzme_skynet.core.driver.web.browsers.phantomjs import PhantomJS
from nzme_skynet.core.driver.web.browsers.remote import Remote


class DriverBuilder(object):

    def __init__(self, driver_type, driver_options, local=True):
        self._driver_type = driver_type
        self._driver_options = driver_options
        self._run_env = local
        self._is_desktop_web = driver_type in DESKTOP_WEBDRIVERS

    def build(self):
        try:
            if self._run_env and self._is_desktop_web:
                return self._build_local_web_driver()
            elif not self._run_env and self._is_desktop_web:
                return self._build_remote_driver()
            elif not self._is_desktop_web:
                return self._build_mobile_web_driver(self._driver_type, self._driver_options, browser="chrome")
        except Exception:
            raise

    def _build_local_web_driver(self):
        driver_init = None
        if self._driver_type == DriverTypes.CHROME:
            driver_init = Chrome(self._driver_options)
        if self._driver_type == DriverTypes.FIREFOX:
            driver_init = FireFox(self._driver_options)
        if self._driver_type == DriverTypes.PHANTOM_JS:
            driver_init = PhantomJS(self._driver_options)
        try:
            return driver_init.create_driver()
        except Exception:
            raise Exception("Failed to initialise local browser driver")

    def _build_mobile_app_driver(self, driver_type, driver_options):
        try:
            driver_init = MApp(mplatform=driver_type, desired_capabilities=driver_options)
            return driver_init.create_driver()
        except Exception:
            raise Exception("{0} not identified, supports only android and ios".format(driver_type))

    def _build_mobile_web_driver(self, driver_type, driver_options=None, browser=None):
        try:
            driver_init = MBrowser(platform=driver_type, desired_capabilities=driver_options, browser=browser)
            return driver_init.create_driver()
        except Exception:
            raise Exception("{0} not identified, supports only android and ios".format(driver_type))

    def _build_remote_driver(self):
        if not self._driver_options:
            if self._driver_type == DriverTypes.CHROME:
                self._driver_options = Chrome.get_default_capability()
            elif self._driver_type == DriverTypes.FIREFOX:
                self._driver_options = FireFox.get_default_capability()
            else:
                raise Exception("Only supports Chrome and Firefox in remote mode when no capabilities passed")
        driver_init = Remote(self._driver_options)
        try:
            return driver_init.create_driver()
        except Exception:
            raise Exception("Failed to initialise remote browser driver")
