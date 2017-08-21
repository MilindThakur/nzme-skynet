# coding=utf-8
import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from nzme_skynet.core.actions.enums.timeouts import DefaultTimeouts


class MobileApp(object):
    action_class = None

    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.driver = None
        self.action = None
        self.logger = logging.getLogger(__name__)

    def init_driver(self):
        self.driver = self._create_webdriver()

    # TODO - Implement mobile actions
    def get_actions(self):
        if not self.action:
            self.action = self._create_actions()
        return self.action

    # TODO - Implement mobile actions
    def _create_actions(self):
        return self.action_class(self.driver)

    def get_page_source(self):
        return self.driver.page_source

    # Naming is not accurate for mobile apps, The method name is shared with the other browser drivers.
    def take_screenshot_current_window(self, _screenshot):
        return self.driver.save_screenshot(_screenshot)

    def get_driver(self):
        return self.driver

    def quit(self):
        self.driver.close_app()

    def get_current_context(self):
        self.driver.contexts

    def get_current_desired_capabilities(self):
        return self.driver.desired_capabilities

    def take_screenshot_current_window(self, filename):
        self.driver.get_screenshot_as_file(filename)

    # MOBILE
    def take_screenshot_mobile(self, filename):
        self.driver.save_screenshot(filename)

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
