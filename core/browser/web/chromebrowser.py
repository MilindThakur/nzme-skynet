from core.browser.browser import *
from selenium.webdriver.chrome.options import Options

class ChromeBrowser(Browser):

    def __init__(self):
        super(ChromeBrowser, self).__init__("chrome", self._defaultChromeOptions())

    def _defaultChromeOptions(self):
        opt = Options()
        # driver.Manage().Window.Maximize() does not work for chrome
        # There is a bug submitted for this on ChromeDriver project.
        opt.add_argument("--start-maximized")
        return opt

    def getBrowserDesiredCapabilities(self):
        raise NotImplementedError