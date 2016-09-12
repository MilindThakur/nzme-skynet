# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import nzme_skynet.core.utils.timeouts as timeout


class Component(object):
    def __init__(self, driver, locator):
        self.driver = driver
        if isinstance(locator, By):
            self.locator = locator
        if isinstance(locator, WebElement):
            self.webelement = locator

    def find_element(self, by=By.CSS_SELECTOR, time=timeout.DEFAULT_TIMEOUT):
        pass

    def find_elements(self):
        pass

    def _find_by_web_elements(self):
        pass

    def is_currently_displayed(self):
        pass

    def will_be_displayed(self):
        pass

    def will_be_displayed_in_time(self, time):
        pass

    def will_be_invisible(self):
        pass

    def will_be_invisible_in_time(self, time):
        pass

    def is_ready_to_interact(self):
        pass

    def will_be_ready_to_interact(self):
        pass

    def will_be_ready_to_interact_in_time(self, time):
        pass

    def is_not_displayed(self):
        pass

    def will_be_not_disaplyed(self):
        pass

    def will_be_not_displayed_in_time(self, time):
        pass

    def exists(self):
        pass

    def is_selected(self):
        pass

    def is_disabled(self):
        pass

    def is_enabled(self):
        pass

    def get_locator(self):
        pass

    def get_attribute(self, attr):
        pass

    def get_text(self):
        pass

    def get_location(self):
        pass

    def click(self):
        pass

    def hover_over(self):
        pass

    def send_keys(self, value):
        pass

    def set_value(self, value):
        pass

    def get_size(self, webElements):
        pass

    def get_element(self, index):
        pass

    def clear(self):
        pass

    def scroll_to_element(self):
        pass

    def execute_script(self, script):
        pass

    def highlight(self):
        pass

    def scroll_and_click(self):
        self.scroll_to_element()
        self.click()
