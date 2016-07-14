class Browser_2(object):
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def createWebdriver(self):
        raise NotImplementedError

    def getBrowserType(self):
        raise NotImplementedError

    def getActions(self):
        raise NotImplementedError

    def initBrowser(self):
        raise NotImplementedError

    def getBaseUrl(self):
        return self.baseUrl

    def setBaseUrl(self, baseUrl):
        self.baseUrl = baseUrl

    def getWebdriver(self):
        raise NotImplementedError

    def getDefaultDesiredCapabilities(self):
        raise NotImplementedError

    def quitWebDriver(self):
        raise NotImplementedError
