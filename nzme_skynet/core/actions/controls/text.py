# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from nzme_skynet.core.actions.controls.component import Component
from nzme_skynet.core.actions.enums.timeouts import DefaultTimeouts


class Text(Component):
    def __init__(self, driver, locator, by=By.CSS_SELECTOR):
        super(Text, self).__init__(driver, locator, by)

    def get_text(self):
        return self.find_element().text

    def currently_has_text(self, text):
        return self.will_have_text(text, time=DefaultTimeouts.SHORT_TIMEOUT)

    def will_have_text(self, text, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            WebDriverWait(self._driver, time).until(ec.text_to_be_present_in_element((self._by, self._locator), text))
            return True
        except Exception:
            return False

    def contains(self, text):
        return self.get_text().contains(text)

    def matches(self, regex):
        return self.get_text().matches(regex)
