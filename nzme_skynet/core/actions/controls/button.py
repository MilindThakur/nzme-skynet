# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component


class Button(Component):
    def __init__(self, driver, by_locator):
        super(Button, self).__init__(driver, by_locator)

    def get_status(self):
        self.get_attribute("value")
