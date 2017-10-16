# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.driverregistry import DriverRegistry
from nzme_skynet.core.pageobject.basepage import BasePage


class BaseWebPage(BasePage):
    page_url = None

    def __init__(self):
        super(BaseWebPage, self).__init__()

    def goto(self, absolute=False):
        DriverRegistry.get_driver().goto_url(self.page_url, absolute)
