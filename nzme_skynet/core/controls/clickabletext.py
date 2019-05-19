# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from nzme_skynet.core.controls.clickable import Clickable
from nzme_skynet.core.controls.enums.timeouts import DefaultTimeouts
import logging
logger = logging.getLogger(__name__)


class ClickableText(Clickable):

    @property
    def text(self):
        self._highlight()
        return self._find_element().text

    def has_text(self, text):
        return self.will_have_text(text, time=DefaultTimeouts.SHORT_TIMEOUT)

    def will_have_text(self, text, time=DefaultTimeouts.LARGE_TIMEOUT):
        try:
            return WebDriverWait(self.driver, time).until(ec.text_to_be_present_in_element((self._by, self._locator),
                                                                                           text))
        except Exception as e:
            logger.debug("Failed to find text {0} for element {1}".format(
                text, self._locator))
            return False
