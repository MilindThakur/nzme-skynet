# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.mobile.browser.mobilebrowser import MobileBrowser
import logging

from nzme_skynet.core.pageobject.ibasepage import IBasePage


class BaseMobilePage(IBasePage):
    page_url = None

    def __init__(self, mwebdriver):
        # type: (MobileBrowser) -> None
        if not isinstance(mwebdriver, MobileBrowser):
            raise TypeError('expected driver to be a MobileBrowser type')
        self.app = mwebdriver
        self.logger = logging.getLogger(__name__)

    def goto(self):
        self.app.goto_relative_url(self.page_url)

    @property
    def locate(self):
        return self.app.action
