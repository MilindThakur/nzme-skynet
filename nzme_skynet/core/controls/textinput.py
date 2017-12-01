# coding=utf-8
from nzme_skynet.core.controls.text import Text


class TextInput(Text):

    def __init__(self, by, locator):
        super(TextInput, self).__init__(by, locator)

    def focus(self):
        raise NotImplementedError

    def clear(self):
        self._highlight()
        self._find_element().clear()

    @property
    def value(self):
        self._highlight()
        return self.get_attribute("value")

    def set_value(self, value):
        self.clear()
        self._find_element().send_keys(value)
