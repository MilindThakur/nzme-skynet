# coding=utf-8
from selenium.webdriver.phantomjs.webdriver import WebDriver

from nzme_skynet.core.browsers.web.browserTypes import BrowserTypes
from nzme_skynet.core.browsers.web.webbrowser import Webbrowser


class PhantomJSBrowser(Webbrowser):
    def __init__(self, baseUrl, windowWidth=None, windowHeight=None, desCap=None):
        super(PhantomJSBrowser, self).__init__(baseUrl, windowHeight=windowHeight, windowWidth=windowWidth)
        self.desCap = desCap

    def get_browser_type(self):
        return BrowserTypes.PHANTOM_JS

    def create_webdriver(self):
        service_args =  ["--ignore-ssl-errors=true",
                         "--ssl-protocol=any",
                         "--web-security=no"
                        ]
        if self.desCap is not None:
            return WebDriver(desired_capabilities=self.desCap, service_args=service_args)
        else:
            return WebDriver(service_args=service_args)
