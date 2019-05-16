# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.mobile.mobiledriver import MobileDriver
from nzme_skynet.core.driver.web.browserdriver import BrowserDriver
import logging
logger = logging.getLogger(__name__)


class MBrowserDriver(MobileDriver, BrowserDriver):

    def __init__(self, desired_capabilities, remote_url='http://127.0.0.1:4444/wd/hub'):
        super(MBrowserDriver, self).__init__(desired_capabilities, remote_url)
        self._browser = self._desired_cap['browserName']

    def add_chrome_options(self, option):
        if "chromeOptions" in self._desired_cap:
            self._desired_cap['chromeOptions']['args'].append(option)
        else:
            self._desired_cap['chromeOptions'] = {'args': [option]}
