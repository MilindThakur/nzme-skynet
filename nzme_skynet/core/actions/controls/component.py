# coding=utf-8
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from nzme_skynet.core.actions.enums.timeouts import DefaultTimeouts


class Component(object):
    def __init__(self, driver, locator, by):
        self.driver = driver
        self.locator = locator
        self.by = by

    def find_element(self):
        return self.driver.find_element(by=self.by, value=self.locator)

    def find_sub_elements(self, by, locator):
        return self.driver.find_element(by=self.by, value=self.locator).find_elements(by=by, value=locator)

    def is_currently_displayed(self):
        return self.will_be_displayed(time=DefaultTimeouts.SHORT_TIMEOUT)

    def will_be_displayed(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            WebDriverWait(self.driver, time).until(ec.presence_of_element_located((self.by, self.locator)))
        except Exception:
            return False
        return True

    def is_not_displayed(self):
        return self.will_not_be_displayed(time=DefaultTimeouts.DEFAULT_TIMEOUT)

    def will_not_be_displayed(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            WebDriverWait(self.driver, time).until(ec.invisibility_of_element_located((self.by, self.locator)))
            return True
        except Exception:
            return False

    def is_ready_to_interact(self):
        return self.will_be_ready_to_interact(time=DefaultTimeouts.DEFAULT_TIMEOUT)

    def will_be_ready_to_interact(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            WebDriverWait(self.driver, time).until(ec.element_to_be_clickable((self.by, self.locator)))
            return True
        except Exception:
            return False

    def currently_has_text(self, text):
        return self.will_have_text(text, time=DefaultTimeouts.SHORT_TIMEOUT)

    def will_have_text(self, text, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            WebDriverWait(self.driver, time).until(ec.text_to_be_present_in_element((self.by, self.locator), text))
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

    def get_attr(self, attr):
        return self.find_element().get_attribute(attr)

    def has_attr(self, attr):
        try:
            self.find_element().get_attribute(attr)
            return True
        except Exception:
            return False

    def get_text(self):
        return self.find_element().text

    def get_location(self):
        return self.find_element().location

    def get_css_property(self, cssproperty):
        return self.driver.value_of_css_property(cssproperty)

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
