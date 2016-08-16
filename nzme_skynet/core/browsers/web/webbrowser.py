# coding=utf-8
from nzme_skynet.core.browsers.browser import Browser


class Webbrowser(Browser):
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
        self.driver = None

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
        if self.baseUrl is not None:
            self.goto_url(self.baseUrl)
        # Any other special settings

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def get_actions(self):
       raise NotImplementedError

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

    def get_webdriver(self):
        return self.driver

    def quit(self):
        self.driver.close()
        self.driver.quit()

    def goto_url(self, url):
        self.driver.get(url)

    def goto_absolute_url(self, url):
        self.baseUrl = url
        self.goto_url(url)

    def goto_relative_url(self, url):
        self.goto_url(self.baseUrl+url)

    def get_current_url(self):
        return self.driver.current_url

    def take_screenshot_current_window(self, filename):
        self.driver.get_screenshot_as_file(filename)

    def take_screenshot_full_page(self, filename):
        # get actual page width
        w_js = "return Math.max(document.body.scrollWidth, document.body.offsetWidth, " \
            "document.documentElement.clientWidth, document.documentElement.scrollWidth, " \
            "document.documentElement.offsetWidth);"
        # get actual page height
        h_js = "return Math.max(document.body.scrollHeight, document.body.offsetHeight, " \
            "document.documentElement.clientHeight, document.documentElement.scrollHeight, " \
            "document.documentElement.offsetHeight);"
        width = self.driver.execute_script(w_js)
        height = self.driver.execute_script(h_js)
        self.driver.set_window_size(width+100, height+100)
        self.take_screenshot_current_window(filename)
