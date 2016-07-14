# coding=utf-8
from selenium import webdriver

from core.browser.sauceconnect import construct_remote_commandexecutor
from core.browser.web.browserTypes import BrowserTypes


class Browser(object):
    def __init__(self, browser, chromeOptions=None, desired_cap=None):
        if browser == BrowserTypes.CHROME:
            self._driver = webdriver.Chrome(chrome_options=chromeOptions)
        if browser == BrowserTypes.FIREFOX:
            self._driver = webdriver.Firefox()
        if browser == BrowserTypes.IE:
            self._driver = webdriver.Ie()
        if browser == BrowserTypes.PHANTOM_JS:
            self._driver = webdriver.PhantomJS()
        if browser == BrowserTypes.SAFARI:
            self._driver = webdriver.Safari()
        if browser == BrowserTypes.REMOTE:
            self._driver = webdriver.Remote(command_executor=construct_remote_commandexecutor(),
                                            desired_capabilities=desired_cap)
        self._driver.maximize_window()
        self._driver.delete_all_cookies()

    def get_webdriver(self):
        return self._driver

    def quit_webdriver(self):
        return self._driver.quit()

    def initialize_webbrowser(self):
        raise NotImplementedError

    def get_browser_type(self):
        return self._driver.name

    def get_title(self):
        return self._driver.title

    def get_current_url(self):
        return self._driver.current_url

    def openurl(self, url):
        return self._driver.get(url)

    def get_browser_desiredcapabilities(self):
        raise NotImplementedError

    @staticmethod
    def is_remote_enabled():
        return False

    def click_browser_back_button(self):
        self._driver.back()

    def browser_refresh(self):
        self._driver.refresh()
