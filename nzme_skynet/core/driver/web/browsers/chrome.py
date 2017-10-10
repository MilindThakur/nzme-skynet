# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from nzme_skynet.core.driver.web.browserdriver import BrowserDriver


class Chrome(BrowserDriver):
    def __init__(self, driver_options):
        self._driver_options = driver_options
        self._options = Options()
        self._driver = None

    @staticmethod
    def get_default_capability():
        return DesiredCapabilities.CHROME.copy()

    def _create_default_chrome_options(self):
        self.add_option("--start-maximized")
        self.add_option("--test-type")
        self.add_option("--disable-notifications")
        self.add_option("-process-per-site")
        self.add_option("--dns-prefetch-disable")

    def _set_options(self):
        self._create_default_chrome_options()
        if self._driver_options:
            for option in self._driver_options:
                self.add_option(option)

    def add_option(self, option):
        self._options.add_argument(option)

    def add_extension(self, extension):
        self._options.add_extension(extension)

    def _create_driver(self):
        self._set_options()
        self._driver = WebDriver(desired_capabilities=DesiredCapabilities.CHROME.copy(),
                                 chrome_options=self._options)

    def get_webdriver(self):
        # type: () -> WebDriver
        if not self._driver:
            raise Exception("Driver has not been created")
        return self._driver
