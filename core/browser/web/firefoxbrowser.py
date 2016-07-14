# coding=utf-8
from core.browser.browser import *


class FirefoxBrowser(Browser):
    def initialize_webbrowser(self):
        pass

    def __init__(self):
        super(FirefoxBrowser, self).__init__("firefox")

    def get_browser_desiredcapabilities(self):
        raise NotImplementedError
