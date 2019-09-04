# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webdriver import WebDriver as RemoteDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging

from nzme_skynet.core.driver.web.browserdriver import BrowserDriver

logger = logging.getLogger(__name__)


class Firefox(BrowserDriver):

    # Allow updating the capability with firefoxOptions
    def _update_capabilities_with_options(self):
        new_ff_options = Options()

        if not self._options:
            logger.debug(
                "No options specified, updating capabilities with default firefox settings")
        else:
            if "mobileEmulation" in self._options:
                logger.warning("mobileEmulation is only available for Chrome")
            if "headless" in self._options and self._options["headless"]:
                new_ff_options.headless = True

        if not self._capabilities:
            logger.debug(
                "No capabilities specified, creating default firefox capability..")
            self._capabilities = DesiredCapabilities.FIREFOX.copy()

        if "marionette" not in self._capabilities:
            self._capabilities["marionette"] = True

        new_ff_cap = new_ff_options.to_capabilities()

        if "moz:firefoxOptions" in self._capabilities and "moz:firefoxOptions" in new_ff_cap:
            for key, value in new_ff_cap["moz:firefoxOptions"].items():
                if not self._capabilities["moz:firefoxOptions"][key] == new_ff_cap["moz:firefoxOptions"][key]:
                    logger.debug(
                        "Updating original capabilities moz:firefoxOptions..")
                    self._capabilities["moz:firefoxOptions"].setdefault(
                        key, []).extend(value)
        elif "moz:firefoxOptions" not in self._capabilities and "moz:firefoxOptions" in new_ff_cap:
            logger.debug(
                "No custom moz:firefoxOptions specified in capabilities, setting default..")
            self._capabilities["moz:firefoxOptions"] = new_ff_cap["moz:firefoxOptions"]

    def _create_driver(self, local, grid_url):
        self._update_capabilities_with_options()
        if not local:
            self._driver = RemoteDriver(
                command_executor=grid_url, desired_capabilities=self._capabilities)
        else:
            self._driver = FirefoxDriver(
                desired_capabilities=self._capabilities)
