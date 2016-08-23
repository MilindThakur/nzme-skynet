# coding=utf-8
from nzme_skynet.core.actions.component import Component


class Button(Component):
    def __init__(self, by_locator):
        super(Button, self).__init__(by_locator)

    def getValue(self):
        pass
