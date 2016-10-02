# coding=utf-8
from selenium.webdriver.common.by import By

from nzme_skynet.core.actions.controls.component import Component
from nzme_skynet.core.actions.enums.checkboxstates import CheckboxState


class Checkbox(Component):
    def __init__(self, driver, locator, by=By.CSS_SELECTOR):
        super(Checkbox, self).__init__(driver, locator, by)

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
