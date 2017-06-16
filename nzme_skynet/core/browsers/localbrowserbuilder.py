# coding=utf-8
from nzme_skynet.core.browsers.mobile.mobilebrowser import MobileBrowser
from nzme_skynet.core.browsers.web.browserTypes import BrowserTypes
from nzme_skynet.core.browsers.web.chromebrowser import ChromeBrowser
from nzme_skynet.core.browsers.web.phantomjsbrowser import PhantomJSBrowser
from nzme_skynet.core.browsers.web.firefoxbrowser import FirefoxBrowser
import selenium
from distutils.version import StrictVersion


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
        try:
            if browserType == BrowserTypes.CHROME:
                return ChromeBrowser(self.baseUrl, self.webDriverPath, self.browserBinaryPath, self.browserVersion,
                                     self.platform, self.windowWidth, self.windowHeight, self.desCap)
            if browserType == BrowserTypes.PHANTOM_JS:
                return PhantomJSBrowser(self.baseUrl, self.windowWidth, self.windowHeight, self.desCap)
            if browserType == BrowserTypes.FIREFOX:
                if StrictVersion(selenium.__version__) > StrictVersion('3.3.1'):
                    return FirefoxBrowser(self.baseUrl, self.windowWidth, self.windowHeight, self.desCap)
                else:
                    raise Exception("Only selenium version > 3.3.1 is supported for marionette Firefox browser, "
                                    "your current version is {0}".format(selenium.__version__))
            if (browserType == BrowserTypes.ANDROID_BROWSER) or (browserType == BrowserTypes.IOS_BROWSER):
                return MobileBrowser(self.desCap, self.baseUrl)
            else:
                raise ValueError("only chrome, firefox, native android and native iphone browsers supported")
        except Exception:
            raise
