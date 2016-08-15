# coding=utf-8
from selenium.webdriver.phantomjs.webdriver import WebDriver

from skynet.core.browsers.web.browserTypes import BrowserTypes
from skynet.core.browsers.web.webbrowser import Webbrowser


class PhantomJSBrowser(Webbrowser):
    def __init__(self, baseUrl, windowWidth=None, windowHeight=None, desCap=None):
        super(PhantomJSBrowser, self).__init__(baseUrl, windowHeight=windowHeight, windowWidth=windowWidth)
        self.desCap = desCap

    def get_browser_type(self):
        return BrowserTypes.PHANTOM_JS

    def create_webdriver(self):
        if self.desCap is not None:
            return WebDriver(desired_capabilities=self.desCap, service_args=['--ssl-protocol=any'])
        else:
            return WebDriver(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])

    def get_actions(self):
        raise NotImplementedError
