# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging

from nzme_skynet.core.driver.web.browserdriver import BrowserDriver

logger = logging.getLogger(__name__)


class Chrome(BrowserDriver):

    # Allow updating the capability with chromeOptions
    def _update_capabilities_with_options(self):
        # Default framework chromeOptions
        _new_chrome_options = {
            "args": ["--test-type",
                     "--disable-notifications",
                     "-process-per-site",
                     "--dns-prefetch-disable"
                     ]
        }
        if not self._options:
            logger.debug(
                "No options specified, updating capabilities with default chrome settings")
        else:
            if "headless" in self._options and self._options["headless"]:
                _new_chrome_options["args"].extend(
                    ["--headless", "--disable-gpu", "--no-sandbox"])

        if not self._capabilities:
            logger.debug(
                "No capabilities specified, creating default chrome capability..")
            self._capabilities = DesiredCapabilities.CHROME.copy()

        # Update chromeOptions using framework defaults
        if "goog:chromeOptions" in self._capabilities:
            self._capabilities["goog:chromeOptions"]['args'] = self._capabilities["goog:chromeOptions"]['args'] + _new_chrome_options['args']
        else:
            self._capabilities["goog:chromeOptions"] = _new_chrome_options

        # Add experimental mobile emulation rendering
        if "mobileEmulation" in self._options and self._options["mobileEmulation"]:
            self._capabilities["goog:chromeOptions"]["mobileEmulation"] = {
                    "deviceName": self._options["mobileEmulation"]}

    def _create_driver(self, local, grid_url):
        self._update_capabilities_with_options()
        if not local:
            self._driver = RemoteDriver(
                command_executor=grid_url, desired_capabilities=self._capabilities)
        else:
            self._driver = ChromeDriver(
                desired_capabilities=self._capabilities)
