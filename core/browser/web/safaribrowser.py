from core.browser.browser import *

class SafariBrowser(Browser):

    def __init__(self):
        super(SafariBrowser, self).__init__("safari")

    def getBrowserDesiredCapabilities(self):
        raise NotImplementedError