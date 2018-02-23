# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.mobile.mobiledriver import MobileDriver
import logging
logger = logging.getLogger(__name__)


class MAppDriver(MobileDriver):

    def __init__(self, desired_capabilities, remote_url='http://127.0.0.1:4444/wd/hub'):
        self._desired_cap = desired_capabilities
        self._remote_url = remote_url
        self._driver = None

    def accept_location_popup(self):
        raise NotImplementedError

    def close_app(self):
        self.webdriver.close_app()

    def is_app_installed(self):
        return self.webdriver.is_app_installed(self.desired_capabilities['appPackage'])

    def _create_desired_capabilities(self):
        raise NotImplementedError

    @property
    def context(self):
        return self.webdriver.context

    def reset(self):
        self.webdriver.reset()

    @property
    def current_running_activity(self):
        return self.webdriver.current_activity

    def wait_for_android_activity(self, activity_name, timeout):
        self.webdriver.wait_activity(activity=activity_name, timeout=timeout)

    def init(self):
        raise NotImplementedError

    def _create_driver(self):
        raise NotImplementedError

    def _set_default_capabilities(self):
        raise NotImplementedError

    def take_screenshot_current_window(self, filename):
        self.webdriver.get_screenshot_as_file(filename)
