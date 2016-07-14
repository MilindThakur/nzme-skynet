# coding=utf-8
from core.browser.browser import *


class SafariBrowser(Browser):
    def __init__(self):
        super(SafariBrowser, self).__init__("safari")

    def get_browser_desiredcapabilities(self):
        raise NotImplementedError
