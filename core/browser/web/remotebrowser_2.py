from core.browser.web.webbrowser import Webbrowser
from selenium.webdriver.remote.webdriver import WebDriver

class RemoteBrowser_2(Webbrowser):

    def __init__(self, browserDel, remoteUrl):
        super(RemoteBrowser_2, self).__init__(browserDel.getBaseUrl(),
                                              browserDel.getWebDriverPath(),
                                              browserDel.getBrowserBinaryPath(),
                                              browserDel.getBrowserVersion(),
                                              browserDel.getPlatform(),
                                              browserDel.getWindowWidth(),
                                              browserDel.getWindowHeight())
        self.delegate = browserDel
        self.remoteUrl = remoteUrl

    def getBrowserType(self):
        return self.delegate.getBrowserType()

    def getDesiredCapabilities(self):
        return self.delegate.getDesiredCapabilities()

    def createWebdriver(self, customCap=None):
        if(customCap is not None):
            driver = WebDriver(command_executor=self.remoteUrl, desired_capabilities=customCap)
        else:
            driver = WebDriver(command_executor=self.remoteUrl, desired_capabilities=self.getDesiredCapabilities())
        return driver

    def getActions(self):
        raise NotImplementedError