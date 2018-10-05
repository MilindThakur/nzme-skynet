# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver


class BaseDriver(object):
    baseurl = None

    def quit(self):
        self.webdriver.quit()

    def close(self):
        self.webdriver.close()

    @property
    def webdriver(self):
        # type: () -> WebDriver
        raise NotImplementedError

    @property
    def desired_capabilities(self):
        return self.webdriver.desired_capabilities()

    @property
    def name(self):
        return self.webdriver.name

    # Browser Specific Interfaces

    @property
    def window_handles(self):
        raise NotImplementedError

    def switch_to_newest_window(self):
        raise NotImplementedError

    def switch_to_oldest_window(self):
        raise NotImplementedError

    @property
    def title(self):
        raise NotImplementedError

    @property
    def current_url(self):
        raise NotImplementedError

    def goto_url(self, url, absolute):
        raise NotImplementedError

    @property
    def page_source(self):
        return self.webdriver.page_source

    def maximize_window(self):
        raise NotImplementedError

    def get_window_size(self):
        raise NotImplementedError

    def set_window_size(self, width, height):
        raise NotImplementedError

    def back(self):
        raise NotImplementedError

    def refresh(self):
        raise NotImplementedError

    def forward(self):
        raise NotImplementedError

    def take_screenshot_current_window(self, filename):
        raise NotImplementedError

    def take_screenshot_full_page(self, filename):
        raise NotImplementedError

    def wait_for_javascript_return(self, script, return_value):
        raise NotImplementedError

    def set_page_load_timeout(self, time):
        raise NotImplementedError

    def switch_to_alert(self, time):
        raise NotImplementedError

    def switch_and_accept_alert(self, time):
        raise NotImplementedError

    def switch_and_dismiss_alert(self, time):
        raise NotImplementedError

    def wait_for_page_load(self, timeout, throw_on_timeout):
        raise NotImplementedError

    @property
    def current_running_activity(self):
        raise NotImplementedError

    def wait_for_activity(self, activity_name, timeout):
        raise NotImplementedError
