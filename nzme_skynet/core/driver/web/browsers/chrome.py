# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.web.browsers.browserdriver import BrowserDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Chrome(BrowserDriver):

    def __init__(self, driver_options):
        self._driver_options = driver_options
        self._options = Options()

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

    def create_driver(self):
        self._set_options()
        return WebDriver(desired_capabilities=DesiredCapabilities.CHROME.copy(),
                         chrome_options=self._options)
