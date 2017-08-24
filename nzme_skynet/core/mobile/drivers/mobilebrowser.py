# coding=utf-8

import logging
from appium import webdriver
from nzme_skynet.core.actions.uiactionsweb import UIActionsWeb
from nzme_skynet.core.browsers.browser import Browser
from nzme_skynet.core.actions.enums.timeouts import DefaultTimeouts


class Mobilebrowser(Browser):
    action_class = UIActionsWeb

    def __init__(self, desired_caps):
        super(Mobilebrowser, self).__init__(desired_caps['selenium_grid_hub'])
        self.selenium_grid_hub_url = desired_caps['selenium_grid_hub']
        self.logger = logging.getLogger(__name__)
        self._desired_caps = desired_caps

    def get_browser_type(self):
        return self.driver.name

    def get_driver_type(self):
        return self.driver.desired_capabilities['platform']

    def get_default_desiredcapabilities(self):
        raise NotImplementedError

    def _create_webdriver(self):
        try:
            return webdriver.Remote(self.selenium_grid_hub_url, self._desired_caps)
        except Exception, e:
            self.logger.debug("Failed to create webdriver instance, Exception:" + str(e.message))
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
