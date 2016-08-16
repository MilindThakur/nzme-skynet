# coding=utf-8
from nzme_skynet.core.browsers.web.browserTypes import BrowserTypes
from nzme_skynet.core.browsers.web.chromebrowser import ChromeBrowser
from nzme_skynet.core.browsers.web.phantomjsbrowser import PhantomJSBrowser


class LocalBrowserBuilder(object):
    def __init__(self, browserType, baseUrl=None, webDriverPath=None, browserBinayPath=None, browserVersion=None,
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
        browser = self._construct_browser(self.browserType)
        browser.init_browser()
        return browser

    def _construct_browser(self, browserType):
        if browserType == BrowserTypes.CHROME:
            return ChromeBrowser(self.baseUrl, self.webDriverPath, self.browserBinaryPath, self.browserVersion,
                                    self.platform, self.windowWidth, self.windowHeight, self.desCap)
        if browserType == BrowserTypes.PHANTOM_JS:
            return PhantomJSBrowser(self.baseUrl, self.windowWidth, self.windowHeight, self.desCap)
        else:
            raise ValueError("only chrome, firefox, safari, ie , phantomJS supported")
