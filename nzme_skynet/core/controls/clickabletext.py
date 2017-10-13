# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from nzme_skynet.core.controls.controls.clickable import Clickable
from nzme_skynet.core.controls.enums.timeouts import DefaultTimeouts


class ClickableText(Clickable):

    def __init__(self, by, locator):
        super(ClickableText, self).__init__(by, locator)

    @property
    def text(self):
        return self._find_element().text

    def currently_has_text(self, text):
        return self.will_have_text(text, time=DefaultTimeouts.SHORT_TIMEOUT)

    def will_have_text(self, text, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            return WebDriverWait(self.driver, time).until(ec.text_to_be_present_in_element((self._by, self._locator),
                                                                                           text))
        except Exception:
            return False

    def contains(self, text):
        return self.text.contains(text)

    def matches(self, regex):
        return self.text.matches(regex)
