from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from core.browser.web.browserTypes import BrowserTypes
from core.browser.web.webbrowser import Webbrowser


class ChromeBrowser_2(Webbrowser):
    def __init__(self, baseUrl, webDriverPath=None, browserBinayPath=None, browserVersion=None, platform=None,
                 windowWidth=None, windowHeight=None, desCap=None):
        super(ChromeBrowser_2, self).__init__(baseUrl, webDriverPath, browserBinayPath, browserVersion, platform,
                                              windowWidth, windowHeight)
        self.desCap = desCap

    def getBrowserType(self):
        return BrowserTypes.CHROME

    def getDefaultDesiredCapabilities(self):
        chrome_options = Options()
        chrome_options.binary_location = self.getBrowserBinaryPath()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--test-type")
        chrome_des_cap = chrome_options.to_capabilities()
        bVersion = self.getBrowserVersion()
        if (bVersion is not None):
            chrome_des_cap["version"] = bVersion
        platform = self.getPlatform()
        if (platform is not None):
            chrome_des_cap["platform"] = platform
        return chrome_des_cap

    def createWebdriver(self):
        driver_path = self.getWebDriverPath()
        if (self.desCap is not None and driver_path is not None):
            return WebDriver(executable_path=driver_path, desired_capabilities=self.desCap)
        if (driver_path is not None):
            return WebDriver(executable_path=driver_path, desired_capabilities=self.getDefaultDesiredCapabilities())
        else:
            return WebDriver(desired_capabilities=self.getDefaultDesiredCapabilities())

    def getActions(self):
        raise NotImplementedError
