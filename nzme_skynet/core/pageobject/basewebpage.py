# -*- coding: utf-8 -*-
from nzme_skynet.core.pageobject.basepage import BasePage


class BaseWebPage(BasePage):
    page_url = None

    def __init__(self):
        super(BaseWebPage, self).__init__()

    def goto(self, absolute=False):
        self.driver.goto_url(self.page_url, absolute)
