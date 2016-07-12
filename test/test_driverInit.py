import unittest
from core.browser.web.chromebrowser import ChromeBrowser
from core.browser.web.firefoxbrowser import FirefoxBrowser
from core.browser.web.phantomjsbrowser import PhantomJSBrowser
from core.browser.web.safaribrowser import SafariBrowser
from core.browser.web.iebrowser import IEBrowser
from core.browser.remoteBrowser import RemoteBrowser
from core.browser.defaultRemoteBrowserCapabilities import testBrowsers

class test_driverInit(unittest.TestCase):

    def test_initChromeWebdriver(self):
        self.dr = ChromeBrowser()
        self._test_initDrivers(self.dr, self.dr.getBrowserType())

    def test_initFirefoxWebDriver(self):
        self.dr = FirefoxBrowser()
        self._test_initDrivers(self.dr, self.dr.getBrowserType())

    def test_initPhantomJSWebDriver(self):
        self.dr = PhantomJSBrowser()
        self._test_initDrivers(self.dr, self.dr.getBrowserType())
    #
    # def test_initSafariWebDriver(self):
    #     self.dr = SafariBrowser()
    #     self._test_initDrivers(self.dr, self.dr.getBrowserType())
    #
    # def test_initIEWebdriver(self):
    #     self.dr = IEBrowser()
    #     self._test_initDrivers(self.dr, self.dr.getBrowserType())

    # def test_initRemoteWebDriver(self):
    #     test_des_cap = testBrowsers[5]
    #     self.dr = RemoteBrowser(test_des_cap)
    #     self._test_initDrivers(self.dr, self.dr.getBrowserType())

    def _test_initDrivers(self, driver, browserName):
        driver.openUrl("https://www.google.com")
        assert driver.getTitle() == "Google"
        assert driver.getBrowserType() == browserName

    def tearDown(self):
        self.dr.quitWebdriver()