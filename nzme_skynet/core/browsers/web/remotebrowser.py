# coding=utf-8
from selenium.webdriver.remote.webdriver import WebDriver

from nzme_skynet.core.browsers.web.webbrowser import Webbrowser


class RemoteBrowser(Webbrowser):

    def __init__(self,  base_url, des_cap,):
        super(RemoteBrowser, self).__init__(base_url)
        self.des_cap = des_cap

    def get_browser_type(self):
        return self.des_cap['browser']

    def get_remote_url(self):
        pass

    def create_webdriver(self):
        return WebDriver(self.get_remote_url(), self.des_cap)

    def get_default_desiredcapabilities(self):
        raise NotImplementedError
