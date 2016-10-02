# coding=utf-8

from nzme_skynet.core.actions.uiactionsweb import UIActionsWeb
from nzme_skynet.core.browsers.browser import Browser


class Webbrowser(Browser):

    action_class = UIActionsWeb

    def __init__(self, baseurl, webDriverPath=None, browserBinayPath=None, browserVersion=None, platform=None,
                 windowWidth=None, windowHeight=None):
        super(Webbrowser, self).__init__(baseurl)
        self.webDriverPath = webDriverPath
        self.browserBinayPath = browserBinayPath
        self.browserVersion = browserVersion
        self.platform = platform
        self.init_window_width = windowWidth
        self.init_window_height = windowHeight

    def get_browser_type(self):
        raise NotImplementedError

    def get_default_desiredcapabilities(self):
        raise NotImplementedError

    def _create_webdriver(self):
        raise NotImplementedError

    def init_browser(self):
        self.driver = self._create_webdriver()
        if self.init_window_height is not None and self.init_window_width is not None:
            self.driver.set_window_size(self.init_window_width, self.init_window_height)
        # TODO: create timeout default class
        self.driver.set_page_load_timeout(80)
        self.driver.implicitly_wait(5)
        if self.baseurl is not None:
            self.goto_url(self.baseurl)
        # Any other special settings

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def get_webdriver_path(self):
        return self.webDriverPath

    def get_browser_binary_path(self):
        return self.browserBinayPath

    def get_browser_version(self):
        return self.browserVersion

    def get_platform(self):
        return self.platform
