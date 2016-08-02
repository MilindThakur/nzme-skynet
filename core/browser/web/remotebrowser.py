# coding=utf-8
from selenium.webdriver.remote.webdriver import WebDriver

from core.browser.web.webbrowser import Webbrowser


class RemoteBrowser(Webbrowser):
    def __init__(self, browserDel, remoteUrl):
        super(RemoteBrowser, self).__init__(browserDel.get_base_url(),
                                            browserDel.get_webdriver_path(),
                                            browserDel.get_browser_binary_path(),
                                            browserDel.get_browser_version(),
                                            browserDel.get_platform(),
                                            browserDel.get_window_width(),
                                            browserDel.get_window_height())
        self.delegate = browserDel
        self.remoteUrl = remoteUrl

    def get_browser_type(self):
        return self.delegate.get_browser_type

    def get_desiredcapabilities(self):
        return self.delegate.get_desiredcapabilities()

    def create_webdriver(self, customCap=None):
        if customCap is not None:
            driver = WebDriver(command_executor=self.remoteUrl, desired_capabilities=customCap)
        else:
            driver = WebDriver(command_executor=self.remoteUrl, desired_capabilities=self.get_desiredcapabilities())
        return driver

    def get_actions(self):
        raise NotImplementedError
