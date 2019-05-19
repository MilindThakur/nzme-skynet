# -*- coding: utf-8 -*-

from nzme_skynet.core.driver.basedriver import BaseDriver
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from nzme_skynet.core.utils import js_wait
from nzme_skynet.core.controls.enums.timeouts import DefaultTimeouts
import logging
from nzme_skynet.core.utils.log import Logger


Logger.configure_logging()
logger = logging.getLogger(__name__)


class BrowserDriver(BaseDriver):
    """
    A base class for web based (browser) drivers
    """

    def __init__(self, capabilities, options):
        self._capabilities = capabilities
        self._options = options
        self._driver = None

    @property
    def webdriver(self):
        # type: () -> WebDriver
        return self._driver

    def goto_url(self, url, absolute=False):
        """
        By default loads page relative to the test url
        :param url:
        :param absolute:
        :return:
        """
        try:
            if absolute:
                self.webdriver.get(url)
            else:
                self.webdriver.get(self.baseurl+url)
        except TimeoutException:
            logger.info("Browser timeout, stopping the window load using js..")
            self.webdriver.execute_script('return window.stop();')

    def _create_driver(self, local, grid_url):
        raise NotImplementedError

    @property
    def title(self):
        return self.webdriver.title

    @property
    def current_url(self):
        return self.webdriver.current_url

    @property
    def window_handles(self):
        return self.webdriver.window_handles

    def switch_to_newest_window(self):
        return self.webdriver.switch_to.window(self.window_handles[len(self.window_handles) - 1])

    def switch_to_oldest_window(self):
        return self.webdriver.switch_to.window(self.window_handles[0])

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

    def add_cookie(self, cookie_dict):
        self.webdriver.add_cookie(cookie_dict)

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
            return self.webdriver.switch_to.alert

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
                until(lambda driver: driver.execute_script(
                    'return document.readyState') == 'complete')
        except TimeoutException:
            if throw_on_timeout:
                raise TimeoutException(
                    "Page elements never fully loaded after %s seconds" % timeout)

    def wait_for_url_to_contain(self, url, time=DefaultTimeouts.LARGE_TIMEOUT):
        """
        Wait until the page url contains the expected url
        :param url: Expected url
        :param time: Timeout to wait for
        :return: True when url matches within timeout period, False otherwise
        """
        try:
            return WebDriverWait(self.webdriver, time).until(expected_conditions.url_contains(url))
        except Exception:
            logger.debug("Failed to find expected url {0} in current url {1}".format(
                url, self.webdriver.current_url))
            return False

    def wait_for_url(self, url, time=DefaultTimeouts.LARGE_TIMEOUT):
        """
        Wait until the page url is same as the expected url
        :param url: Expected url
        :param time: Timeout to wait for
        :return: True when url matches exactly within timeout period, False otherwise
        """
        try:
            return WebDriverWait(self.webdriver, time).until(expected_conditions.url_matches(url))
        except Exception:
            logger.debug("Failed to match expected url {0} to current url {1}".format(
                url, self.webdriver.current_url))
            return False

    def init(self, local, grid_url):
        """
        Initialize webdriver based on browserName in capability. Also set the window size based on
        resolution as "maximum" or e.g. "1900x1200"
        """
        self._create_driver(local, grid_url)
        self.webdriver.set_page_load_timeout(DefaultTimeouts.PAGE_LOAD_TIMEOUT)
        if self._options and self._options["resolution"]:
            if self._options["resolution"] == "maximum":
                self.webdriver.maximize_window()
            else:
                width = self._options["resolution"].split("x")[0]
                height = self._options["resolution"].split("x")[1]
                self.webdriver.set_window_size(width, height)
