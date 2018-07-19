# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from nzme_skynet.core.driver.web.browserdriver import BrowserDriver


class Chrome(BrowserDriver):
    def __init__(self, driver_capabilities, headless=False):
        self.driver_capabilities = driver_capabilities
        self._options = Options()
        self._driver = None
        self._headless = headless

    @staticmethod
    def get_default_capability(headless=False):
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--test-type")
        options.add_argument("--disable-notifications")
        options.add_argument("-process-per-site")
        options.add_argument("--dns-prefetch-disable")
        if headless:
            options.headless = True
        return options.to_capabilities()

    def _create_default_chrome_options(self):
        self.add_option("--start-maximized")
        self.add_option("--test-type")
        self.add_option("--disable-notifications")
        self.add_option("-process-per-site")
        self.add_option("--dns-prefetch-disable")
        # Load pages without Images
        # self._options.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
        if self._headless:
            self.add_option("--headless")

        # TODO - Implement this
        if self.driver_capabilities and 'viewport' in self.driver_capabilities:
            # check for known list of devices and set appropriate device name.

            # match found
            # use this to consume the known device name
            # mobile_emulation = {"deviceName" = > "Nexus 5"}
            # self.add_experimental_option("mobileEmulation", mobile_emulation)

            # No match found
            # if no name is returned then set width x height

            pass

    def _set_options(self):
        self._create_default_chrome_options()

    def add_option(self, option):
        self._options.add_argument(option)

    def add_extension(self, extension):
        self._options.add_extension(extension)

    def _create_driver(self):
        self._set_options()
        self._driver = WebDriver(desired_capabilities=DesiredCapabilities.CHROME.copy(),
                                 chrome_options=self._options)

    @property
    def webdriver(self):
        # type: () -> WebDriver
        return self._driver
