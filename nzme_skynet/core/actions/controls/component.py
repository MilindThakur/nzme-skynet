# coding=utf-8
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from nzme_skynet.core.actions.enums.timeouts import DefaultTimeouts


class Component(object):
    def __init__(self, driver, locator, by):
        self.driver = driver
        self.locator = locator
        self.by = by

    def find_element(self):
        return self.driver.find_element(by=self.by, value=self.locator)

    def get_webelement(self):
        return self.find_element()

    def find_elements(self):
        return self.driver.find_elements(by=self.by, value=self.locator)

    def is_currently_displayed(self):
        return self.will_be_displayed(DefaultTimeouts.SHORT_TIMEOUT)

    def will_be_displayed(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(self.locator))
            return True
        except Exception:
            return False

    def is_not_displayed(self):
        return self.will_not_be_displayed(DefaultTimeouts.DEFAULT_TIMEOUT)

    def will_not_be_displayed(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            WebDriverWait(self.driver, time).until(expected_conditions.invisibility_of_element_located(self.locator))
            return True
        except Exception:
            return False

    def is_ready_to_interact(self):
        return self.will_be_ready_to_interact(DefaultTimeouts.DEFAULT_TIMEOUT)

    def will_be_ready_to_interact(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(self.locator))
            return True
        except Exception:
            return False

    def exists(self):
        try:
            self.find_element()
            return True
        except Exception:
            return False

    def is_selected(self):
        return self.find_element().is_selected()

    def is_disabled(self):
        return not self.find_element().is_enabled()

    def is_enabled(self):
        return self.find_element().is_enabled()

    def get_locator(self):
        return self.locator

    def get_attribute(self, attr):
        return self.find_element().get_attribute(attr)

    def get_text(self):
        return self.find_element().text

    def get_location(self):
        return self.find_element().location

    def click(self):
        self.find_element().click()

    def hover_over(self):
        elem = self.find_element()
        hover = ActionChains(self.driver).move_to_element(elem)
        hover.perform()

    def send_keys(self, value):
        self.find_element().send_keys(value)

    def set_value(self, value):
        self.send_keys(value)

    # TODO
    # def get_size(self, webElements):
    #     raise NotImplementedError

    def clear(self):
        self.find_element().clear()

    def scroll_to_element(self, offset=200):
        loc = self.get_location()
        self.driver.execute_script("window.scrollBy(0," + str(loc['y'] - offset) + ");")

    # TODO
    # def highlight(self):
    #     raise NotImplementedError

    def scroll_and_click(self):
        self.scroll_to_element()
        self.click()
