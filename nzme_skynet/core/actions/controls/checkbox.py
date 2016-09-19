# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component
from nzme_skynet.core.actions.enums.checkboxstates import CheckboxState


class Checkbox(Component):
    def __init__(self, driver, by_locator):
        super(Checkbox, self).__init__(driver, by_locator)

    def set(self, checkbox_state):
        if checkbox_state == CheckboxState.CHECKED:
            self.check()
        else:
            self.uncheck()

    def check(self):
        if not super(Checkbox, self).is_selected():
            super(Checkbox, self).click()

    def uncheck(self):
        if super(Checkbox, self).is_selected():
            super(Checkbox, self).click()

    def is_checked(self):
        return super(Checkbox, self).is_selected()
