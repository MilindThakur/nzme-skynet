# coding=utf-8
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


from nzme_skynet.core.actions.enums.timeouts import DefaultTimeouts


class Component(object):
    def __init__(self, driver, locator, by):
        self._driver = driver
        self._locator = locator
        self._by = by

    def find_element(self):
        return self._driver.find_element(by=self._by, value=self._locator)

    def find_sub_elements(self, by, locator):
        return self._driver.find_element(by=self._by, value=self._locator).find_elements(by=by, value=locator)

    def is_currently_visible(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        return self.will_be_visible(time=time)

    def will_be_visible(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            WebDriverWait(self._driver, time).until(ec.visibility_of_element_located((self._by, self._locator)))
        except Exception:
            return False
        return True

    def is_currently_present(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        return self.will_be_present(time=time)

    def will_be_present(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            WebDriverWait(self._driver, time).until(ec.presence_of_element_located((self._by, self._locator)))
        except Exception:
            return False
        return True

    def is_not_displayed(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        return self.will_not_be_displayed(time=time)

    def will_not_be_displayed(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            WebDriverWait(self._driver, time).until(ec.invisibility_of_element_located((self._by, self._locator)))
            return True
        except Exception:
            return False

    def is_ready_to_interact(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        return self.will_be_ready_to_interact(time=time)

    def will_be_ready_to_interact(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            WebDriverWait(self._driver, time).until(ec.element_to_be_clickable((self._by, self._locator)))
            return True
        except Exception:
            return False

    def currently_has_text(self, text, time=DefaultTimeouts.SHORT_TIMEOUT):
        return self.will_have_text(text, time=time)

    def will_have_text(self, text, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            WebDriverWait(self._driver, time).until(ec.text_to_be_present_in_element((self._by, self._locator), text))
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
        return self._locator

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
        return self._driver.value_of_css_property(cssproperty)

    def click(self):
        self.is_ready_to_interact()
        self.find_element().click()

    def hover_over(self):
        elem = self.find_element()
        hover = ActionChains(self._driver).move_to_element(elem)
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
        self._driver.execute_script("window.scrollBy(0," + str(loc['y'] - offset) + ");")

    # TODO
    # def highlight(self):
    #     raise NotImplementedError

    def scroll_and_click(self):
        self.scroll_to_element()
        self.click()
