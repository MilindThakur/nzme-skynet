# coding=utf-8
from selenium.webdriver.remote.webdriver import WebDriver

from nzme_skynet.core.browsers.web.webbrowser import Webbrowser


class RemoteBrowser(Webbrowser):

    def __init__(self, base_url, des_cap,):
        super(RemoteBrowser, self).__init__(base_url)
        self.des_cap = des_cap

    def get_browser_type(self):
        return self.des_cap['browser']

    def get_remote_url(self):
        pass

    def _create_webdriver(self):
        return WebDriver(desired_capabilities=self.des_cap)

    def get_platform_name(self):
        try:
            return self.des_cap['platformName']
        except KeyError:
            return None

    def get_platform_version(self):
        try:
            return str(self.des_cap['platformVersion'])
        except KeyError:
            return None

    def get_default_desiredcapabilities(self):
        raise NotImplementedError
