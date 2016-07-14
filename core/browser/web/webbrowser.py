from core.browser.browser_2 import Browser_2


class Webbrowser(Browser_2):

    def __init__(self, baseUrl, webDriverPath=None, browserBinayPath=None, browserVersion=None, platform=None,
                 windowWidth=None, windowHeight=None):
        super(Webbrowser, self).__init__(baseUrl)
        self.webDriverPath = webDriverPath
        self.browserBinayPath = browserBinayPath
        self.browserVersion = browserVersion
        self.platform = platform
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

    def getBrowserType(self):
        raise NotImplementedError

    def getDefaultDesiredCapabilities(self):
        raise NotImplementedError

    def initBrowser(self):
        self.driver = self.createWebdriver()
        if(self.windowHeight is not None and self.windowWidth is not None):
            self.driver.set_window_size(self.windowWidth, self.windowHeight)
        # TODO: create timeout default class
        self.driver.set_page_load_timeout(80)
        self.driver.implicitly_wait(5)
        # Any other special settings

    def getWebDriverPath(self):
        return self.webDriverPath

    def getBrowserBinaryPath(self):
        return self.browserBinayPath

    def getBrowserVersion(self):
        return self.browserVersion

    def getPlatform(self):
        return self.platform

    def getWindowWidth(self):
        return self.windowWidth

    def getWindowHeight(self):
        return self.windowHeight

    def refreshPage(self):
        self.driver.refresh()

    def cleanSession(self):
        self.driver.delete_all_cookies()

    def getWebdriver(self):
        return self.driver

    def quitWebDriver(self):
        self.driver.quit()