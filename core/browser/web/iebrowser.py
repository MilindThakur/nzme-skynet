# coding=utf-8
from core.browser.browser import Browser


class IEBrowser(Browser):
    def __init__(self):
        super(IEBrowser, self).__init__("ie")

    def get_browser_desiredcapabilities(self):
        raise NotImplementedError
