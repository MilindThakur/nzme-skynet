# -*- coding: utf-8 -*-
from nzme_skynet.core.actions.enums.timeouts import DefaultTimeouts


class BrowserDriver(object):
    """
    A base abstract class for web based (browser) drivers
    """

    def _create_driver(self):
        raise NotImplementedError

    @property
    def webdriver(self):
        raise NotImplementedError

    def add_option(self, option):
        raise NotImplementedError

    def add_extension(self, extension):
        raise NotImplementedError

    @staticmethod
    def get_default_capability():
        raise NotImplementedError

    def set_proxy(self):
        # TODO: Implemented here
        pass

    def init(self):
        self._create_driver()
        self.webdriver.maximize_window()
        self.webdriver.set_page_load_timeout(DefaultTimeouts.PAGE_LOAD_TIMEOUT)
