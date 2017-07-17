# coding=utf-8
from nzme_skynet.core.browsers.web.browserTypes import BrowserTypes
from nzme_skynet.core.browsers.web.chromebrowser import ChromeBrowser
from nzme_skynet.core.browsers.web.firefoxbrowser import FirefoxBrowser
from nzme_skynet.core.browsers.web.phantomjsbrowser import PhantomJSBrowser


class LocalBrowserBuilder(object):
    def __init__(self, browser_options, baseUrl=None):
        self.baseUrl = baseUrl
        self.browser_options = browser_options
        self._browserType = browser_options.get('type')

    def build(self):
        browser = self._construct_browser()
        browser.init_browser()
        return browser

    def _construct_browser(self):
        try:
            if self._browserType == BrowserTypes.CHROME:
                return ChromeBrowser(self.baseUrl, **self.browser_options)
            if self._browserType == BrowserTypes.PHANTOM_JS:
                return PhantomJSBrowser(self.baseUrl, **self.browser_options)
            if self._browserType == BrowserTypes.FIREFOX:
                # if StrictVersion(selenium.__version__) > StrictVersion('3.3.1'):
                    return FirefoxBrowser(self.baseUrl, **self.browser_options)
                # else:
                #     raise Exception("Only selenium version > 3.3.1 is supported for marionette Firefox browser, "
                #                     "your current version is {0}".format(selenium.__version__))
            if (self._browserType == BrowserTypes.ANDROID_BROWSER) or (self._browserType == BrowserTypes.IOS_BROWSER):
                raise NotImplementedError
            else:
                raise ValueError("only chrome, firefox, phantomjs browsers are supported")
        except Exception:
            raise
