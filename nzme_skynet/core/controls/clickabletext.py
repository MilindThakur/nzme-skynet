# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from nzme_skynet.core.controls.clickable import Clickable
from nzme_skynet.core.controls.enums.timeouts import DefaultTimeouts
import logging
logger = logging.getLogger(__name__)


class ClickableText(Clickable):
    """
    This class extends Clickable class and contains methods that help in identifying the text attribute of the element

    :param by: type of locator
    :param locator: locator value
    """

    def __init__(self, by, locator):
        super(ClickableText, self).__init__(by, locator)

    @property
    def text(self):
        """
        This method helps in highlighting and returning the text of the element when it is present and visible. And
        return false when the element is not present and visible.
        :return: text or False
        """
        self._highlight()
        return self._find_element().text

    def has_text(self, text):
        """
        This method validate the existence of text within the element within 1 second and returns the same in
        successful case. And returns False with a debug log if the text in the element.

        :param text: text that is expected to be present
        :return: text or False
        """
        return self.will_have_text(text, time=DefaultTimeouts.SHORT_TIMEOUT)

    def will_have_text(self, text, time=DefaultTimeouts.LARGE_TIMEOUT):
        """
        This method validate the existence of text within the element within 10 seconds and returns the same in
        successful case. And returns False with a debug log if the text in the element.

        :param text: text that is expected to be present
        :param time: defaulted to LARGE_TIMEOUT period of 10 seconds
        :return: text or False
        """
        try:
            return WebDriverWait(self.driver, time).until(ec.text_to_be_present_in_element((self._by, self._locator),
                                                                                           text))
        except Exception as e:
            logger.debug("Failed to find text {0} for element {1}".format(text, self._locator))
            return False
