from core.browser.browser import Browser

class IEBrowser(Browser):

    def __init__(self):
        super(IEBrowser, self).__init__("ie")

    def getBrowserDesiredCapabilities(self):
        raise NotImplementedError