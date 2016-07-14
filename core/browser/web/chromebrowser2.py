# coding=utf-8
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from core.browser.web.browserTypes import BrowserTypes
from core.browser.web.webbrowser import Webbrowser


class ChromeBrowser2(Webbrowser):
    def __init__(self, baseurl, webDriverPath=None, browserBinayPath=None, browserVersion=None, platform=None,
                 windowWidth=None, windowHeight=None, desCap=None):
        super(ChromeBrowser2, self).__init__(baseurl, webDriverPath, browserBinayPath, browserVersion, platform,
                                             windowWidth, windowHeight)
        self.desCap = desCap

    def get_browser_type(self):
        return BrowserTypes.CHROME

    def get_default_desiredcapabilities(self):
        chrome_options = Options()
        chrome_options.binary_location = self.get_browser_binary_path()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--test-type")
        chrome_des_cap = chrome_options.to_capabilities()
        b_version = self.get_browser_version()
        if b_version is not None:
            chrome_des_cap["version"] = b_version
        platform = self.get_platform()
        if platform is not None:
            chrome_des_cap["platform"] = platform
        return chrome_des_cap

    def create_webdriver(self):
        driver_path = self.get_webdriver_path()
        if self.desCap is not None and driver_path is not None:
            return WebDriver(executable_path=driver_path, desired_capabilities=self.desCap)
        if driver_path is not None:
            return WebDriver(executable_path=driver_path, desired_capabilities=self.get_default_desiredcapabilities())
        else:
            return WebDriver(desired_capabilities=self.get_default_desiredcapabilities())

    def get_actions(self):
        raise NotImplementedError
