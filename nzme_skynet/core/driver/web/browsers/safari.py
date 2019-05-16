from nzme_skynet.core.driver.web.browserdriver import BrowserDriver
from selenium.webdriver.safari.webdriver import WebDriver as SafariDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging

logger = logging.getLogger(__name__)


# noinspection PyAbstractClass
class Safari(BrowserDriver):

    # Allow updating the capability with firefoxOptions
    def _update_capabilities_with_options(self):
        if not self._options:
            logger.debug(
                "No options specified, updating capabilities with default  settings")
        else:
            if "mobileEmulation" in self._options:
                logger.warning("mobileEmulation is only available for Chrome")
            if "headless" in self._options:
                logger.warning(
                    "No capability to run Safari in a headless mode")

        if not self._capabilities:
            logger.debug(
                "No capabilities specified, creating default safari capability..")
            self._capabilities = DesiredCapabilities.SAFARI.copy()

    def _create_driver(self, local, grid_url):
        self._update_capabilities_with_options()
        if not local:
            self._driver = RemoteDriver(
                command_executor=grid_url, desired_capabilities=self._capabilities)
        else:
            self._driver = SafariDriver(
                desired_capabilities=self._capabilities)
