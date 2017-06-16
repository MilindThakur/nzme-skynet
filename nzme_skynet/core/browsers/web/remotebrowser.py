# coding=utf-8
from selenium.webdriver.remote.webdriver import WebDriver
import logging
from selenium.common.exceptions import WebDriverException
from nzme_skynet.core.browsers.web.webbrowser import Webbrowser


class RemoteBrowser(Webbrowser):
    def __init__(self, command_executor, des_cap, base_url):
        super(RemoteBrowser, self).__init__(base_url)
        self.command_executor = command_executor
        self.des_cap = des_cap
        self.logger = logging.getLogger(__name__)

    def get_browser_type(self):
        return self.des_cap['browserName']

    def get_remote_url(self):
        pass

    def _create_webdriver(self):
        self.logger.debug("Instantiating a browser of type {0} with version {1} on os {2}".
                          format(self.get_browser_type(), self.get_platform_version(), self.get_platform_name()))
        try:
            return WebDriver(command_executor=self.command_executor, desired_capabilities=self.des_cap)
        except Exception:
            self.logger.exception("Failed to instantiate browser {0} in grid, "
                                  "please check if the grid is running".format(self.get_browser_type()))
            raise

    def get_platform_name(self):
        try:
            return self.des_cap['platform']
        except KeyError:
            return None

    def get_platform_version(self):
        try:
            return str(self.des_cap['version'])
        except KeyError:
            return None

    def get_default_desiredcapabilities(self):
        raise NotImplementedError
