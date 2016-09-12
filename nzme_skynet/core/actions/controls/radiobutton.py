# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component


class RadioButton(Component):
    def __init__(self, driver, by_locator):
        super(RadioButton, self).__init__(driver, by_locator)

    def get_value(self):
        pass
