# coding=utf-8
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.webdriver import WebDriver
import selenium
from distutils.version import StrictVersion

from nzme_skynet.core.browsers.web.webbrowser import Webbrowser


class FirefoxBrowser(Webbrowser):
    def __init__(self, baseurl, **kwargs):
        super(FirefoxBrowser, self).__init__(baseurl, **kwargs)

    def get_default_desiredcapabilities(self):
        # DesiredCapabilities.FIREFOX.copy() sets marionette internally if using geckodriver
        capabilities = DesiredCapabilities.FIREFOX.copy()
        # Selenium Py 3.3.1 has issues running Firefox with geckodriver on desktop.
        # We use v3.3.1 for Zalenium in grid mode.
        # Remove the 'marionette' capability before passing to Firefox Webdriver.
        if StrictVersion(selenium.__version__) == StrictVersion('3.3.1'):
            capabilities.pop('marionette')
        return capabilities

    def _create_webdriver(self):
        try:
            return WebDriver(capabilities=self.get_default_desiredcapabilities())
        except Exception:
            raise
