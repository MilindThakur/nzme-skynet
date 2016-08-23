# coding=utf-8
from nzme_skynet.core.actions.component import Component


class Checkbox(Component):
    def __init__(self, by_locator):
        super(Checkbox, self).__init__(by_locator)

    def set(self, checkBoxState):
        pass

    def check(self):
        pass

    def uncheck(self):
        pass

    def isChecked(self):
        pass
