from selenium import webdriver
from core.browser.sauceconnect import constructRemoteCommandExecutor
from core.browser.web.browserTypes import BrowserTypes
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Browser(object):

    def __init__(self, browser, chromeOptions=None, desired_cap=None):
        if browser == BrowserTypes.CHROME:
            self._driver = webdriver.Chrome(chrome_options=chromeOptions)
        if browser == BrowserTypes.FIREFOX:
            self._driver = webdriver.Firefox()
        if browser == BrowserTypes.IE:
            self._driver = webdriver.Ie()
        if browser == BrowserTypes.PHANTOM_JS:
            self._driver = webdriver.PhantomJS()
        if browser == BrowserTypes.SAFARI:
            self._driver = webdriver.Safari()
        if browser == BrowserTypes.REMOTE:
            self._driver = webdriver.Remote(command_executor=constructRemoteCommandExecutor(),
                                            desired_capabilities=desired_cap)
        self._driver.maximize_window()
        self._driver.delete_all_cookies()

    def getWebDriver(self):
        return self._driver

    def quitWebdriver(self):
        return self._driver.quit()

    def initializeWebBrowser(self):
        raise NotImplementedError

    def getBrowserType(self):
        return self._driver.name

    def getTitle(self):
        return self._driver.title

    def getCurrentUrl(self):
        return self._driver.current_url

    def openUrl(self, url):
        return self._driver.get(url)

    def getBrowserDesiredCapabilities(self):
        raise NotImplementedError

    def isRemoteEnabled(self):
        return False

    def clickBrowserBackButton(self):
        self._driver.back()

    def browserRefresh(self):
        self._driver.refresh()