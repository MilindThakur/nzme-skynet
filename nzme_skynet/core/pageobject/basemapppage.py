# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.mobile.app.mobileapp import MobileApp
import logging

from nzme_skynet.core.pageobject.ibasepage import IBasePage


class BaseMAppPage(IBasePage):

    def __init__(self, nzmedriver):
        # type: (MobileApp) -> None
        if not isinstance(nzmedriver, MobileApp):
            raise TypeError('expected driver to be a MobileApp type')
        self.app = nzmedriver
        self.logger = logging.getLogger(__name__)

    @property
    def locate(self):
        return self.app.action
