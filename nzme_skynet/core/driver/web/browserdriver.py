# -*- coding: utf-8 -*-

from nzme_skynet.core.driver.basedriver import BaseDriver
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from nzme_skynet.core.utils import js_wait
from nzme_skynet.core.actions.enums.timeouts import DefaultTimeouts


class BrowserDriver(BaseDriver):
    """
    A base abstract class for web based (browser) drivers
    """

    def goto_url(self, url, absolute=False):
        """
        By default loads page relative to the test url
        :param url:
        :param absolute:
        :return:
        """
        if absolute:
            self.webdriver.get(url)
        else:
            self.webdriver.get(url)

    def _create_driver(self):
        raise NotImplementedError

    def add_option(self, option):
        raise NotImplementedError

    def add_extension(self, extension):
        raise NotImplementedError

    @staticmethod
    def get_default_capability():
        raise NotImplementedError

    def set_proxy(self):
        # TODO: Implemented here
        pass

    @property
    def title(self):
        return self.webdriver.title

    @property
    def page_source(self):
        return self.webdriver.page_source

    @property
    def current_url(self):
        return self.webdriver.current_url

    def maximize_window(self):
        self.webdriver.maximize_window()

    def get_window_size(self):
        return self.webdriver.get_window_size()

    def set_window_size(self, width, height):
        self.webdriver.set_window_size(width, height)

    def back(self):
        self.webdriver.back()

    def refresh(self):
        self.webdriver.refresh()

    def forward(self):
        self.webdriver.forward()

    def take_screenshot_current_window(self, filename):
        self.webdriver.get_screenshot_as_file(filename)

    def take_screenshot_full_page(self, filename):
        # get actual page width
        w_js = "return Math.max(document.body.scrollWidth, document.body.offsetWidth, " \
               "document.documentElement.clientWidth, document.documentElement.scrollWidth, " \
               "document.documentElement.offsetWidth);"
        # get actual page height
        h_js = "return Math.max(document.body.scrollHeight, document.body.offsetHeight, " \
               "document.documentElement.clientHeight, document.documentElement.scrollHeight, " \
               "document.documentElement.offsetHeight);"
        width = self.webdriver.execute_script(w_js)
        height = self.webdriver.execute_script(h_js)
        self.webdriver.set_window_size(width + 100, height + 100)
        self.take_screenshot_current_window(filename)

    def wait_for_javascript_return(self, script, return_value):
        return WebDriverWait(self.webdriver, 10).until(js_wait.for_return(script, return_value))

    def set_page_load_timeout(self, time=DefaultTimeouts.DEFAULT_TIMEOUT):
        self.webdriver.set_page_load_timeout(time)

    def switch_to_alert(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        if WebDriverWait(self.webdriver, time).until(expected_conditions.alert_is_present()):
            return self.webdriver.switch_to_alert()

    def switch_and_accept_alert(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        alert = self.switch_to_alert(time)
        return alert.accept

    def switch_and_dismiss_alert(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        alert = self.switch_to_alert(time)
        return alert.dismiss

    def wait_for_page_load(self, timeout=DefaultTimeouts.DEFAULT_TIMEOUT, throw_on_timeout=False):
        """
        Waits for the current document to load (although AJAX and other loads might still be happening)
        :param timeout: Time to wait for document to load, seconds
        :param throw_on_timeout: Boolean to throw exception when timeout is reached
        """
        try:
            WebDriverWait(self.webdriver, timeout).\
                until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        except TimeoutException:
            if throw_on_timeout:
                raise TimeoutException("Page elements never fully loaded after %s seconds" % timeout)

    def init(self):
        self._create_driver()
        self.webdriver.maximize_window()
        self.webdriver.set_page_load_timeout(DefaultTimeouts.PAGE_LOAD_TIMEOUT)
