# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.mobile.mobileDriver import MobileDriver


class MAppDriver(MobileDriver):

    def close_app(self):
        self.webdriver.close_app()

    def is_app_installed(self):
        return self.webdriver.is_app_installed(self.desired_capabilities['appPackage'])

    def _create_desired_capabilities(self):
        raise NotImplementedError

    @property
    def context(self):
        return self.webdriver.context

    def _create_driver(self):
        raise NotImplementedError

    def reset(self):
        self.webdriver.reset()

    @property
    def current_running_activity(self):
        return self.webdriver.current_activity

    def wait_for_android_activity(self, activity_name, timeout):
        self.webdriver.wait_activity(activity=activity_name, timeout=timeout)

    def init(self):
        self._create_driver()
