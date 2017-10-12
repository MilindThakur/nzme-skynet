# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.basedriver import BaseDriver


class MAppDriver(BaseDriver):

    def close_app(self):
        self.webdriver.close_app()

    def is_app_installed(self):
        return self.webdriver.is_app_installed(self.desired_capabilities['appPackage'])

    def launch_app(self):
        self.webdriver.launch_app()

    @property
    def context(self):
        return self.webdriver.context

    def _create_driver(self):
        raise NotImplementedError
