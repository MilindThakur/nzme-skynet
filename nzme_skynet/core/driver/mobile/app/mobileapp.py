# coding=utf-8
import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from nzme_skynet.core.actions.enums.timeouts import DefaultTimeouts
from nzme_skynet.core.actions.uiactionsmob import UIActionsMob
from appium import webdriver


class MobileApp(object):

    def __init__(self, desired_caps):
        self._desired_caps = desired_caps
        self.driver = None
        self._action = None
        self.logger = logging.getLogger(__name__)

    def init_driver(self):
        try:
            self.driver = webdriver.Remote(self._desired_caps['selenium_grid_hub'], self._desired_caps)
        except Exception, e:
            self.logger.exception("Failed to launch appium driver, Exception: {0}".format(e))
            raise

    def is_app_installed(self):
        return self.driver.is_app_installed(self._desired_caps['appPackage'])

    def get_driver_type(self):
        return self.driver.desired_capabilities['platform']

    @property
    def action(self):
        if not self._action:
            self._action = UIActionsMob(self.driver)
        return self._action

    def get_page_source(self):
        return self.driver.page_source

    def get_driver(self):
        return self.driver

    def quit(self):
        self.driver.close_app()
        self.driver.quit()

    def get_current_context(self):
        return self.driver.contexts

    def get_current_desired_capabilities(self):
        return self.driver.desired_capabilities

    # Naming is not accurate for mobile apps, The method name is shared with the other browser drivers.
    def take_screenshot_current_window(self, filename):
        self.driver.get_screenshot_as_file(filename)

    # TODO - These are nice to haves.
    # def switch_to_alert(self, time=DefaultTimeouts.SHORT_TIMEOUT):
    #     if WebDriverWait(self.driver, time).until(expected_conditions.alert_is_present()):
    #         return self.driver.switch_to_alert()
    #
    # def switch_and_accept_alert(self, time=DefaultTimeouts.SHORT_TIMEOUT):
    #     alert = self.switch_to_alert(time)
    #     return alert.accept
    #
    # def switch_and_dismiss_alert(self, time=DefaultTimeouts.SHORT_TIMEOUT):
    #     alert = self.switch_to_alert(time)
    #     return alert.dismiss

    # TODO - experimental. may not work at all
    def wait_for_page_change(self, timeout=DefaultTimeouts.DEFAULT_TIMEOUT, throw_on_timeout=False):
        """
        Waits for the page source to change, indicating that the action has resulted in a visible change
        :param timeout: Time to wait for the page change to occurr, seconds
        :param throw_on_timeout: Boolean to throw exception when timeout is reached
        """
        try:
            WebDriverWait(self.driver, timeout). \
                until(self.get_page_source() != self.get_page_source())
        except:
            if throw_on_timeout:
                raise TimeoutException("Page elements never fully loaded after %s seconds" % timeout)
