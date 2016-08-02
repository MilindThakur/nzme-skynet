# coding=utf-8
from selenium.webdriver.phantomjs.webdriver import WebDriver

from core.browser.web.browserTypes import BrowserTypes
from core.browser.web.webbrowser import Webbrowser


class PhantomJSBrowser(Webbrowser):
    def __init__(self, baseUrl, windowWidth=None, windowHeight=None, desCap=None):
        super(PhantomJSBrowser, self).__init__(baseUrl, windowHeight=windowHeight, windowWidth=windowWidth)
        self.desCap = desCap

    def get_browser_type(self):
        return BrowserTypes.PHANTOM_JS

    def create_webdriver(self):
        if self.desCap is not None:
            return WebDriver(desired_capabilities=self.desCap)
        else:
            return WebDriver()

    def get_actions(self):
        raise NotImplementedError
