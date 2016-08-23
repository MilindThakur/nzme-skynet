# coding=utf-8
from nzme_skynet.core.actions.component import Component


class Input(Component):
    def __init__(self, by_locator):
        super(Input, self).__init__(by_locator)

    def get_value(self):
        pass

    def set_value(self, value):
        pass

    def clear(self):
        pass
