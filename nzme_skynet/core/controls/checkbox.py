# coding=utf-8
from nzme_skynet.core.controls.clickable import Clickable
from nzme_skynet.core.controls.enums.checkboxstates import CheckboxState


class Checkbox(Clickable):

    def set(self, checkbox_state):
        """
        Check/uncheck checkbox element based on parameter
        :param checkbox_state: bool
        :Example:

        checkbox = Checkbox(By.ID, "checkbox_id")
        checkbox.set(True)
        checkbox.is_checked()   # => True
        checkbox.set(False)
        checkbox.is_checked()   # => False
        """
        if checkbox_state == CheckboxState.CHECKED:
            self.check()
        else:
            self.uncheck()

    def is_checked(self):
        """
        Return if checkbox is checked
        :return: bool
        """
        return self._find_element().is_selected()

    def check(self):
        """
        Check the checkbox element
        """
        if not self.is_checked():
            self.click()

    def uncheck(self):
        """
        Uncheck the checkbox element
        :return:
        """
        if self.is_checked():
            self.click()
