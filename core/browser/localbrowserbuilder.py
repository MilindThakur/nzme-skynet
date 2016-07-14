from core.browser.web.browserTypes import BrowserTypes
from core.browser.web.chromebrowser_2 import ChromeBrowser_2


class LocalBrowserBuilder(object):
    def __init__(self, browserType, baseUrl, webDriverPath=None, browserBinayPath=None, browserVersion=None,
                 platform=None, windowWidth=None, windowHeight=None, desCap=None):
        # if browserType is None:
        #   raise StandardError
        self.browserType = browserType
        self.baseUrl = baseUrl
        self.webDriverPath = webDriverPath
        self.browserBinaryPath = browserBinayPath
        self.browserVersion = browserVersion
        self.platform = platform
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.desCap = desCap

    def build(self):
        if self.browserType == BrowserTypes.CHROME:
            browser = ChromeBrowser_2(self.baseUrl, self.webDriverPath, self.browserBinaryPath, self.browserVersion,
                                      self.platform, self.windowWidth, self.windowHeight, self.desCap)
        else:
            raise ValueError("only chrome, firefox, safari, ie , phantomJS supported")
        browser.initBrowser()
        return browser
