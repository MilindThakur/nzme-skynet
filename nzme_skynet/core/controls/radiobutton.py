# coding=utf-8
from nzme_skynet.core.controls.button import Button


class RadioButton(Button):

    def is_selected(self):
        self._highlight()
        return self._find_element().is_selected()
