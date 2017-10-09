# coding=utf-8
from selenium.webdriver.common.by import By

from nzme_skynet.core.actions.controls.clickable import Clickable
from nzme_skynet.core.actions.enums.checkboxstates import CheckboxState


class Checkbox(Clickable):
    def __init__(self, driver, locator, by=By.CSS_SELECTOR):
        super(Checkbox, self).__init__(driver, locator, by)

    def set(self, checkbox_state):
        if checkbox_state == CheckboxState.CHECKED:
            self.check()
        else:
            self.uncheck()

    def is_checked(self):
        return self.find_element().is_selected()

    def check(self):
        if not self.is_checked():
            self.click()

    def uncheck(self):
        if self.is_checked():
            self.click()
