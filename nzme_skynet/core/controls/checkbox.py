# coding=utf-8
from nzme_skynet.core.controls.clickable import Clickable
from nzme_skynet.core.controls.enums.checkboxstates import CheckboxState


class Checkbox(Clickable):

    def __init__(self, by, locator):
        super(Checkbox, self).__init__(by, locator)

    def set(self, checkbox_state):
        if checkbox_state == CheckboxState.CHECKED:
            self.check()
        else:
            self.uncheck()

    def is_checked(self):
        return self._find_element().is_selected()

    def check(self):
        if not self.is_checked():
            self.click()

    def uncheck(self):
        if self.is_checked():
            self.click()
