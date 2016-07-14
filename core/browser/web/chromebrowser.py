# coding=utf-8
from selenium.webdriver.chrome.options import Options

from core.browser.browser import *


class ChromeBrowser(Browser):
    def initialize_webbrowser(self):
        pass

    def __init__(self):
        super(ChromeBrowser, self).__init__("chrome", self._default_chrome_options())

    # noinspection PyMethodMayBeStatic
    def _default_chrome_options(self):
        opt = Options()
        # driver.Manage().Window.Maximize() does not work for chrome
        # There is a bug submitted for this on ChromeDriver project.
        opt.add_argument("--start-maximized")
        return opt

    def get_browser_desiredcapabilities(self):
        raise NotImplementedError
