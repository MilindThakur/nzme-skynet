# coding=utf-8
from core.browser.browser import *


class PhantomJSBrowser(Browser):
    def __init__(self):
        super(PhantomJSBrowser, self).__init__("phantomJS")

    def get_browser_desiredcapabilities(self):
        raise NotImplementedError
