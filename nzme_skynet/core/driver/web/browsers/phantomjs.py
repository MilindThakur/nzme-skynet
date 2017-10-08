# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.web.browsers.browserdriver import BrowserDriver
from selenium.webdriver.phantomjs.webdriver import WebDriver


class PhantomJS(BrowserDriver):

    def __init__(self, driver_options):
        self._driver_options = driver_options
        self._service_args = None

    def add_option(self, option):
        pass

    def _create_default_phantonjs_options(self):
        self._service_args = ["--ignore-ssl-errors=true",
                              "--ssl-protocol=any",
                              "--web-security=no"
                              ]

    def _set_options(self):
        self._create_default_phantonjs_options()
        for arg in self._driver_options:
            self._service_args.add(arg)

    def add_extension(self, extension):
        # Not Extensions are available for phantomjs
        pass

    def create_driver(self):
        self._set_options()
        return WebDriver(service_args=self._service_args)
