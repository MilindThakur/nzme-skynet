# coding=utf-8
from nzme_skynet.core.controls.button import Button


class RadioButton(Button):

    def __init__(self, by, locator):
        super(RadioButton, self).__init__(by, locator)

    def is_selected(self):
        return self._find_element().is_selected()
