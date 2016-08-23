# coding=utf-8
from nzme_skynet.core.actions.component import Component


class Table(Component):
    def __init__(self, by_locator):
        super(Table, self).__init__(by_locator)
