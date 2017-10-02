# -*- coding: utf-8 -*-
import logging
from nzme_skynet.core.driver.web.browsers.webbrowser import Webbrowser
from nzme_skynet.core.pageobject.ibasepage import IBasePage


class BaseWebPage(IBasePage):
    page_url = None

    def __init__(self, nzmedriver):
        # type: (Webbrowser) -> None
        if not isinstance(nzmedriver, Webbrowser):
            raise TypeError('expect driver to be a Webbrowser type')
        self.page = nzmedriver
        self.logger = logging.getLogger(__name__)

    def goto(self, relative=True):
        self.page.goto_url(self.page_url, relative)

    @property
    def locate(self):
        return self.page.action
