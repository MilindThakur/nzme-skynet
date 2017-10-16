# -*- coding: utf-8 -*-
import logging

from nzme_skynet.core.driver.driverregistry import DriverRegistry


class BasePage(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    @property
    def driver(self):
        return DriverRegistry.get_driver()