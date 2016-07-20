# coding=utf-8
from core.browser.browser2 import Browser2


class Webbrowser(Browser2):
    def create_webdriver(self):
        pass

    def __init__(self, baseurl, webDriverPath=None, browserBinayPath=None, browserVersion=None, platform=None,
                 windowWidth=None, windowHeight=None):
        super(Webbrowser, self).__init__(baseurl)
        self.webDriverPath = webDriverPath
        self.browserBinayPath = browserBinayPath
        self.browserVersion = browserVersion
        self.platform = platform
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

    def get_browser_type(self):
        raise NotImplementedError

    def get_default_desiredcapabilities(self):
        raise NotImplementedError

    def init_browser(self):
        self.driver = self.create_webdriver()
        if self.windowHeight is not None and self.windowWidth is not None:
            self.driver.set_window_size(self.windowWidth, self.windowHeight)
        # TODO: create timeout default class
        self.driver.set_page_load_timeout(80)
        self.driver.implicitly_wait(5)
        self.goto_url(self.baseUrl)

        # Any other special settings

    def get_actions(self):
        pass

    def get_webdriver_path(self):
        return self.webDriverPath

    def get_browser_binary_path(self):
        return self.browserBinayPath

    def get_browser_version(self):
        return self.browserVersion

    def get_platform(self):
        return self.platform

    def get_window_width(self):
        return self.windowWidth

    def get_window_height(self):
        return self.windowHeight

    def refresh_page(self):
        self.driver.refresh()

    def clean_session(self):
        self.driver.delete_all_cookies()

    def get_webdriver(self):
        return self.driver

    def quit_webdriver(self):
        self.driver.quit()

    def goto_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url
