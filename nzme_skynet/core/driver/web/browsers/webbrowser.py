# coding=utf-8

import logging

from nzme_skynet.core.actions.uiactionsweb import UIActionsWeb
from nzme_skynet.core.driver.web.browser import Browser
from nzme_skynet.core.actions.enums.timeouts import DefaultTimeouts


class Webbrowser(Browser):

    def __init__(self, baseurl, **kwargs):
        super(Webbrowser, self).__init__(baseurl)
        self._init_browser_window_width = kwargs.get('windowwidth')
        self._init_browser_window_height = kwargs.get('windowheight')
        self.logger = logging.getLogger(__name__)

    def get_default_desiredcapabilities(self):
        raise NotImplementedError

    def _create_webdriver(self):
        raise NotImplementedError

    @property
    def action(self):
        # type: () -> UIActionsWeb
        if not self._action:
            self._action = UIActionsWeb(self.driver)
        return self._action

    def init_driver(self):
        self.driver = self._create_webdriver()
        # TODO - Make this more robust and not use driver.capabilities
        if self.driver.capabilities['browserName']:
            if self._init_browser_window_height and self._init_browser_window_width:
                self.driver.set_window_size(self._init_browser_window_width, self._init_browser_window_height)
            else:
                self.logger.debug("No default window size found, setting to maximise")
                self.driver.maximize_window()
        # TODO: create timeout default class
        self.driver.set_page_load_timeout(DefaultTimeouts.PAGE_LOAD_TIMEOUT)
        # self.driver.implicitly_wait(5)
        if self.baseurl is not None:
            self.goto_url(self.baseurl, relative=False)
        # Any other special settings

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

