# -*- coding: utf-8 -*-
import logging
from nzme_skynet.core.driver.web.browsers.webbrowser import Webbrowser
from nzme_skynet.core.pageobject.ibasepage import IBasePage


class BaseWebPage(IBasePage):
    page_url = None

    def __init__(self, webdriver):
        # type: (Webbrowser) -> None
        if not isinstance(webdriver, Webbrowser):
            raise TypeError('expect driver to be a Webbrowser type')
        self.app = webdriver
        self.logger = logging.getLogger(__name__)

    def goto(self):
        self.app.goto_relative_url(self.page_url)

    @property
    def locate(self):
        return self.app.action
