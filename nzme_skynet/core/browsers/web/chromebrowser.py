# coding=utf-8
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from nzme_skynet.core.browsers.web.browserTypes import BrowserTypes
from nzme_skynet.core.browsers.web.webbrowser import Webbrowser


class ChromeBrowser(Webbrowser):
    def __init__(self, baseurl, webDriverPath=None, browserBinayPath=None, browserVersion=None, platform=None,
                 windowWidth=None, windowHeight=None, desCap=None):
        super(ChromeBrowser, self).__init__(baseurl, webDriverPath, browserBinayPath, browserVersion, platform,
                                            windowWidth, windowHeight)
        self.des_cap = desCap

    def get_browser_type(self):
        return BrowserTypes.CHROME

    def get_default_desiredcapabilities(self):
        chrome_options = Options()
        chrome_options.binary_location = self.get_browser_binary_path()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("-process-per-site")
        chrome_options.add_argument("--dns-prefetch-disable")
        chrome_des_cap = chrome_options.to_capabilities()
        b_version = self.get_browser_version()
        if b_version is not None:
            chrome_des_cap["version"] = b_version
        platform = self.get_platform()
        if platform is not None:
            chrome_des_cap["platform"] = platform
        return chrome_des_cap

    def _create_webdriver(self):
        # TODO: can add binary path to chrome, if required
        driver_path = self.get_webdriver_path()
        try:
            if self.des_cap is not None and driver_path is not None:
                return WebDriver(executable_path=driver_path, desired_capabilities=self.des_cap)
            if driver_path is not None:
                return WebDriver(executable_path=driver_path, desired_capabilities=self.get_default_desiredcapabilities())
            else:
                return WebDriver(desired_capabilities=self.get_default_desiredcapabilities())
        except Exception:
            raise
