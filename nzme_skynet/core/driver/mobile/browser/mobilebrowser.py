# coding=utf-8

import logging
from appium import webdriver
from nzme_skynet.core.actions.uiactionsmob import UIActionsMob
from nzme_skynet.core.driver.web.browser import Browser
from nzme_skynet.core.actions.enums.timeouts import DefaultTimeouts


class MobileBrowser(Browser):

    def __init__(self, desired_caps):
        super(MobileBrowser, self).__init__(desired_caps['baseUrl'])
        self._desired_caps = desired_caps.pop('baseUrl')
        self.logger = logging.getLogger(__name__)

    def get_browser_type(self):
        return self.driver.name

    @property
    def action(self):
        if not self._action:
            self._action = UIActionsMob(self.driver)
        return self._action

    def get_driver_type(self):
        return self.driver.desired_capabilities['platform']

    def get_default_desiredcapabilities(self):
        raise NotImplementedError

    def _create_webdriver(self):
        try:
            return webdriver.Remote(self._desired_caps['selenium_grid_hub'], self._desired_caps)
        except Exception, e:
            self.logger.exception("Failed to create webdriver instance, Exception:" + str(e.message))
            raise

    def init_driver(self):
        self.driver = self._create_webdriver()
        # TODO: create timeout default class
        self.driver.set_page_load_timeout(DefaultTimeouts.PAGE_LOAD_TIMEOUT)
        self.driver.implicitly_wait(5)

    def get_browser_version(self):
        return self.driver.capabilities['version']

    def get_browser_platform(self):
        return self.driver.capabilities['platform']

    def init_browser(self):
        raise NotImplementedError
