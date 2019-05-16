# -*- coding: utf-8 -*-
from appium.webdriver.webdriver import WebDriver
from nzme_skynet.core.driver.basedriver import BaseDriver
import logging
logger = logging.getLogger(__name__)


class MobileDriver(BaseDriver):

    def __init__(self, desired_capabilities, remote_url='http://127.0.0.1:4444/wd/hub'):
        self._desired_cap = desired_capabilities
        self._remote_url = remote_url
        self._driver = None

    def pinch_and_zoom(self):
        raise NotImplementedError

    def swipe(self):
        raise NotImplementedError

    def scroll(self):
        raise NotImplementedError

    def take_screenshot_current_window(self, filename):
        self.webdriver.get_screenshot_as_file(filename)

    @property
    def webdriver(self):
        # type: () -> WebDriver
        return self._driver

    def init(self):
        if not self._driver:
            self._create_driver()

    def _create_driver(self):
        logger.debug("Creating Mobile driver..")
        self._create_desired_capabilities()
        self._driver = WebDriver(
            command_executor=self._remote_url, desired_capabilities=self._desired_cap)

    def _create_desired_capabilities(self):
        raise NotImplementedError

    @property
    def context(self):
        return self.webdriver.context
