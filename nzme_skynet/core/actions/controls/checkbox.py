# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component


class Checkbox(Component):
    def __init__(self, driver, by_locator):
        super(Checkbox, self).__init__(driver, by_locator)

    def set(self, checkBoxState):
        pass

    def check(self):
        pass

    def uncheck(self):
        pass

    def is_checked(self):
        pass
