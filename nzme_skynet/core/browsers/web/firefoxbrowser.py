# coding=utf-8
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from nzme_skynet.core.browsers.web.browserTypes import BrowserTypes
from nzme_skynet.core.browsers.web.webbrowser import Webbrowser


class FirefoxBrowser(Webbrowser):
    def __init__(self, baseurl, webDriverPath=None, browserBinayPath=None, browserVersion=None, platform=None,
                 windowWidth=None, windowHeight=None, desCap=None):
        super(FirefoxBrowser, self).__init__(baseurl, webDriverPath, browserBinayPath, browserVersion, platform,
                                            windowWidth, windowHeight)
        self.des_cap = desCap

    def get_browser_type(self):
        return BrowserTypes.FIREFOX

    def get_default_desiredcapabilities(self):
        capabilities = DesiredCapabilities.FIREFOX.copy()
        capabilities['marionette'] = 'True'
        return capabilities

    def _create_webdriver(self):
        driver_path = self.get_webdriver_path()
        try:
            if self.des_cap is not None and driver_path is not None:
                return WebDriver(executable_path=driver_path, capabilities=self.get_default_desiredcapabilities())
            if self.des_cap is not None:
                return WebDriver(capabilities=self.des_cap)
            else:
                return WebDriver(capabilities=self.get_default_desiredcapabilities())
        except Exception:
            raise
