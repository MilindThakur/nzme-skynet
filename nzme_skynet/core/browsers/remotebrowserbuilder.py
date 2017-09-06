# coding=utf-8
from nzme_skynet.core.browsers.web.remotebrowser import RemoteBrowser
import logging


class RemoteBrowserBuilder(object):
    def __init__(self, sel_grid_url, desired_capabilities, base_url):
        self.command_executor = sel_grid_url
        self.desired_capabilities = desired_capabilities
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)

    def build(self):
        browser = self._construct_remote_browser()
        browser.init_browser()
        self.logger.debug("Successfully initialised browser {0}".format(self.desired_capabilities['browserName']))
        return browser

    def _construct_remote_browser(self):
        return RemoteBrowser(self.command_executor,  self.desired_capabilities, self.base_url)
