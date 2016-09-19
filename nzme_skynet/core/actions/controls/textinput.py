# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component


class TextInput(Component):
    def __init__(self, driver, by_locator):
        super(TextInput, self).__init__(driver, by_locator)

    def get_value(self):
        return self.get_attribute("value")

    def clear(self):
        super(TextInput, self).clear()
