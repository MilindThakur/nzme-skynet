# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.mobile.mobileDriver import MobileDriver
from nzme_skynet.core.driver.web.browserdriver import BrowserDriver


class MBrowserDriver(MobileDriver, BrowserDriver):

    def some_function(self):
        raise NotImplementedError
