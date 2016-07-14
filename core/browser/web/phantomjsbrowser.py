from core.browser.browser import *


class PhantomJSBrowser(Browser):
    def __init__(self):
        super(PhantomJSBrowser, self).__init__("phantomJS")

    def getBrowserDesiredCapabilities(self):
        raise NotImplementedError
