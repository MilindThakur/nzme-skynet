# coding=utf-8
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from nzme_skynet.core.actions.enums.timeouts import DefaultTimeouts


class Browser(object):
    action_class = None

    def __init__(self, baseurl, driver=None, action=None):
        self.baseurl = baseurl
        self.driver = driver
        self.action = action

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

    def refresh_page(self):
        self.driver.refresh()

    def get_webdriver(self):
        return self.driver

    def quit(self):
        self.driver.close()
        self.driver.quit()

    def goto_url(self, url):
        self.baseurl = url
        self.driver.get(url)

    def goto_absolute_url(self, url):
        self.baseurl = url
        self.goto_url(url)

    def goto_relative_url(self, url):
        self.goto_url(self.baseurl + url)

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
