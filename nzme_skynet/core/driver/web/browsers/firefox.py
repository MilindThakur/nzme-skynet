# -*- coding: utf-8 -*-
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver

from nzme_skynet.core.driver.web.browserdriver import BrowserDriver


class FireFox(BrowserDriver):
    def __init__(self, driver_options):
        self._driver_options = driver_options
        self._profile = FirefoxProfile()
        self._options = Options()
        self._driver = None

    @staticmethod
    def get_default_capability():
        return DesiredCapabilities.FIREFOX.copy()

    def _create_default_firefox_options(self):
        pass

    def add_option(self, option):
        self._options.add_argument(option)

    def _set_options(self):
        self._create_default_firefox_options()
        if self._driver_options:
            for option in self._driver_options:
                self.add_option(option)

    def add_extension(self, extension):
        self._profile.add_extension(extension)

    def _create_driver(self):
        self._set_options()
        self._driver = WebDriver(firefox_profile=self._profile,
                                 firefox_options=self._options,
                                 capabilities=DesiredCapabilities.FIREFOX.copy())

    @property
    def webdriver(self):
        # type: () -> WebDriver
        return self._driver
