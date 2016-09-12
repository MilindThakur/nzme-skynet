# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component


class Elem(Component):
    def __init__(self, driver, by_locator):
        super(Elem, self).__init__(driver, by_locator)
