# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.mobile.browser.mobilebrowser import MobileBrowser
import logging

from nzme_skynet.core.pageobject.ibasepage import IBasePage


class BaseMobilePage(IBasePage):
    page_url = None

    def __init__(self, nzmedriver):
        # type: (MobileBrowser) -> None
        if not isinstance(nzmedriver, MobileBrowser):
            raise TypeError('expected driver to be a MobileBrowser type')
        self.page = nzmedriver
        self.logger = logging.getLogger(__name__)

    def goto(self, relative=True):
        self.page.goto_url(self.page_url, relative)

    @property
    def locate(self):
        return self.page.action
