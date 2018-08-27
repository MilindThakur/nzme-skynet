# -*- coding: utf-8 -*-
from nzme_skynet.core.controls.baseelement import BaseElement
import logging
from nzme_skynet.core.utils.log import Logger


Logger.configure_logging()
logger = logging.getLogger(__name__)


class Clickable(BaseElement):
    """
    This class extends BaseElement class and contains methods that help in
    performing different type of click actions by utilising the properties defined in BaseClass

    :param by: type of locator
    :param locator: locator value
    """

    def __init__(self, by, locator):
        super(Clickable, self).__init__(by, locator)

    def click(self):
        """
        This method highlights and performs click action on the web element when it is present and visible.
        Returns False with a debug log when the element is not present.

        :return: perform click action or False
        """
        self.is_ready_to_interact()
        self._highlight()
        self._find_element().click()

    def clickjs(self):
        """
        This method synchronously executes the JavaScript to perform click action when the element is present and
        returns False with a debug log when the element is not present.
        action

        :return: perform click action or False
        """
        try:
            self.driver.execute_script("arguments[0].click();", self._find_element())
        except Exception as e:
            logger.debug("Element {0} is not present in the DOM".format(self._locator))
            return False

    def scroll_and_click(self):
        """
        This method invokes the JavaScript to scroll to the element and then perform click action when the element is
        present. Returns False with a debug log when the element is not present.

        :return: perform click action or False
        """
        try:
            self.scroll_to_element()
            self.click()
        except Exception as e:
            logger.debug("Element {0} is not present in the DOM".format(self._locator))
            return False

    def click_parent(self):
        self._find_element().find_element_by_xpath('..').click()
