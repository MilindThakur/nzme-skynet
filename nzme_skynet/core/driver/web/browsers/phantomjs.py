# -*- coding: utf-8 -*-
from selenium.webdriver.phantomjs.webdriver import WebDriver

from nzme_skynet.core.driver.web.browserdriver import BrowserDriver


class PhantomJS(BrowserDriver):

    def __init__(self, driver_options):
        self._driver_options = driver_options
        self._service_args = None
        self._driver = None

    def add_option(self, option):
        self._service_args.append(option)

    def _create_default_phantomjs_options(self):
        self._service_args = ["--ignore-ssl-errors=true",
                              "--ssl-protocol=any",
                              "--web-security=no"
                              ]

    def _set_options(self):
        self._create_default_phantomjs_options()
        if self._driver_options:
            for arg in self._driver_options:
                self.add_option(arg)

    def add_extension(self, extension):
        # Not Extensions are available for phantomjs
        pass

    def _create_driver(self):
        self._set_options()
        self._driver = WebDriver(service_args=self._service_args)

    @property
    def webdriver(self):
        # type: () -> WebDriver
        return self._driver

    @staticmethod
    def get_default_capability():
        pass
