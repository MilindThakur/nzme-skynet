# coding=utf-8
from nzme_skynet.core.controls.clickable import Clickable
from nzme_skynet.core.controls.enums.checkboxstates import CheckboxState
import logging
from nzme_skynet.core.utils.log import Logger


Logger.configure_logging()
logger = logging.getLogger(__name__)

class Checkbox(Clickable):
    """
    This class extends Clickable class and contains methods that help in performing different actions with Checkbox

    :param by: type of locator
    :param locator: locator value

    Usage Example:

        color_checkbox = Checkbox(By.ID, "uniqueID")

        color_checkbox.set("CHECKED")
        color_checkbox.check()
        color_checkbox.uncheck()
        assert color_checkbox.is_checked()
        color_checkbox.is_currently_visible()

    """

    def __init__(self, by, locator):
        super(Checkbox, self).__init__(by, locator)

    def set(self, checkbox_state):
        if checkbox_state == CheckboxState.CHECKED:
            self.check()
        else:
            self.uncheck()

    def is_checked(self):
        """
        This method helps to identify if the element (checkbox) is selected. Returns 1 when the element is selected and
        0 when the element is not selected.
        :return: 1 or 0
        """
        return self._find_element().is_selected()

    def check(self):
        """
        This method validates if the element (checkbox) is not checked and performs click action on the
        element (checkbox)
        """
        if not self.is_checked():
            self.click()

    def uncheck(self):
        """
        This method validates if the element (checkbox) is checked and performs click action on the
        element (checkbox) to uncheck the same.
        :return:
        """
        if self.is_checked():
            self.click()
