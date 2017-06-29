# coding=utf-8
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from nzme_skynet.core.browsers.web.webbrowser import Webbrowser


class ChromeBrowser(Webbrowser):
    def __init__(self, baseurl, **kwargs):
        super(ChromeBrowser, self).__init__(baseurl, **kwargs)
        self._browser_version = kwargs.get('version')
        self._browser_os = kwargs.get('os')

    def get_default_desiredcapabilities(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("-process-per-site")
        chrome_options.add_argument("--dns-prefetch-disable")
        return chrome_options

    def create_chrome_capabilities(self):
        cap = DesiredCapabilities.CHROME.copy()
        cap['version'] = self._browser_version
        cap['platform'] = self._browser_os
        return cap

    def _create_webdriver(self):
        try:
            return WebDriver(desired_capabilities=self.create_chrome_capabilities(),
                             chrome_options=self.get_default_desiredcapabilities())
        except Exception:
            raise
