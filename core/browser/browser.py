# coding=utf-8
class Browser(object):
    def __init__(self, baseurl):
        self.baseUrl = baseurl

    def create_webdriver(self):
        raise NotImplementedError

    def get_browser_type(self):
        raise NotImplementedError

    def get_actions(self):
        raise NotImplementedError

    def init_browser(self):
        raise NotImplementedError

    def get_base_url(self):
        return self.baseUrl

    def set_base_url(self, baseUrl):
        self.baseUrl = baseUrl

    def get_webdriver(self):
        raise NotImplementedError

    def get_default_desiredcapabilities(self):
        raise NotImplementedError

    def quit_webdriver(self):
        raise NotImplementedError
