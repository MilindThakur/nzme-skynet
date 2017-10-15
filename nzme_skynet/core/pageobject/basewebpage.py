# -*- coding: utf-8 -*-
import logging

from nzme_skynet.core.driver.driverregistry import DriverRegistry


class BaseWebPage(object):
    page_url = None

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def goto(self, absolute=False):
        DriverRegistry.get_driver().goto_url(self.page_url, absolute)

    @property
    def driver(self):
        return DriverRegistry.get_driver()
