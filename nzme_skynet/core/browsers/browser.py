# coding=utf-8
import logging

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from nzme_skynet.core.actions.enums.timeouts import DefaultTimeouts
from nzme_skynet.core.utils import js_wait


class Browser(object):
    action_class = None

    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.driver = None
        self.action = None
        self.logger = logging.getLogger(__name__)

    def init_browser(self):
        raise NotImplementedError

    def set_base_url(self, baseurl):
        self.baseurl = baseurl

    def get_actions(self):
        if not self.action:
            self.action = self._create_actions()
        return self.action

    def _create_actions(self):
        return self.action_class(self.driver)

    def get_current_window_size(self):
        return self.driver.get_window_size()

    def get_window_handles(self):
        return self.driver.window_handles

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_newest_window(self):
        return self.driver.switch_to.window(self.get_window_handles()[len(self.get_window_handles()) - 1])

    def switch_to_oldest_window(self):
        try:
            return self.driver.switch_to.window(self.get_window_handles()[0])
        except Exception, e:
            self.logger.debug("Failed switching back to oldest window. " + e.message)
            raise

    def refresh_page(self):
        self.driver.refresh()

    def get_webdriver(self):
        return self.driver

    def quit(self):
        self.driver.quit()

    def goto_url(self, url):
        self.baseurl = url
        try:
            self.driver.get(url)
        except TimeoutException:
            self.logger.warning("Browser load timed out after {0} secs, stopping browser load using JS"
                                .format(str(DefaultTimeouts.PAGE_LOAD_TIMEOUT)))
            self.driver.execute_script("window.stop();")

    def goto_absolute_url(self, url):
        self.baseurl = url
        self.goto_url(url)

    def goto_relative_url(self, url):
        self.goto_url(self.baseurl + url)

    def get_current_url(self):
        return self.driver.current_url

    def get_current_desired_capabilities(self):
        return self.driver.desired_capabilities

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
        self.driver.set_window_size(width + 100, height + 100)
        self.take_screenshot_current_window(filename)

    def switch_to_frame(self, webelement):
        self.driver.switch_to_frame(webelement)

    def switch_to_default_frame(self):
        self.driver.switch_to_default_content()

    def get_cookie(self, cookie):
        return self.driver.get_cookie(cookie)

    def get_all_cookies(self):
        return self.driver.get_cookies()

    def add_cookie(self, cookie):
        self.driver.add_cookie(cookie)

    def delete_local_storage(self):
        self.driver.execute_script('window.localStorage.clear();')

    def switch_to_alert(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        if WebDriverWait(self.driver, time).until(expected_conditions.alert_is_present()):
            return self.driver.switch_to_alert()

    def switch_and_accept_alert(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        alert = self.switch_to_alert(time)
        return alert.accept

    def switch_and_dismiss_alert(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        alert = self.switch_to_alert(time)
        return alert.dismiss

    def wait_for_javascript_return(self, script, return_value):
        return WebDriverWait(self.driver, 10).until(self._wait_for_js(script, return_value))

    def wait_for_page_load(self, timeout=DefaultTimeouts.DEFAULT_TIMEOUT, throw_on_timeout=False):
        """
        Waits for the current document to load (although AJAX and other loads might still be happening)
        :param timeout: Time to wait for document to load, seconds
        :param throw_on_timeout: Boolean to throw exception when timeout is reached
        """
        try:
            WebDriverWait(self.driver, timeout).\
                until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        except:
            if throw_on_timeout:
                raise TimeoutException("Page elements never fully loaded after %s seconds" % timeout)

    def _wait_for_js(self, script, return_value):
        return js_wait.for_return(script, return_value)
