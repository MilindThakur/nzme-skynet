# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.mobile.mobileDriver import MobileDriver
from appium.webdriver.webdriver import WebDriver


class MAppDriver(MobileDriver):

    def __init__(self, desired_capabilities, remote_url='http://127.0.0.1:4444/wd/hub'):
        self._desired_cap = desired_capabilities
        self._remote_url = remote_url
        self._driver = None

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
        self._create_driver()

    def _create_driver(self):
        self._driver = WebDriver(command_executor=self._remote_url, desired_capabilities=self._desired_cap)

    def _set_default_capabilities(self):
        self._create_desired_capabilities()
        self._desired_cap['fullReset'] = 'True'

    @property
    def webdriver(self):
        # type: () -> WebDriver
        return self._driver
