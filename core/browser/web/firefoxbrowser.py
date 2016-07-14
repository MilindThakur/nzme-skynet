from core.browser.browser import *


class FirefoxBrowser(Browser):
    def __init__(self):
        super(FirefoxBrowser, self).__init__("firefox")

    def getBrowserDesiredCapabilities(self):
        raise NotImplementedError
