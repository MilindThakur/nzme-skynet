# coding=utf-8
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.webdriver import WebDriver

from nzme_skynet.core.browsers.web.webbrowser import Webbrowser


class FirefoxBrowser(Webbrowser):
    def __init__(self, baseurl, **kwargs):
        super(FirefoxBrowser, self).__init__(baseurl, **kwargs)

    def get_default_desiredcapabilities(self):
        capabilities = DesiredCapabilities.FIREFOX.copy()
        capabilities['marionette'] = 'True'
        return capabilities

    def _create_webdriver(self):
        try:
            return WebDriver(capabilities=self.get_default_desiredcapabilities())
        except Exception:
            raise
