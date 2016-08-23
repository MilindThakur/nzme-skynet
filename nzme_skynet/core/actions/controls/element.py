# coding=utf-8
from nzme_skynet.core.actions.component import Component


class Element(Component):
    def __init__(self, by_locator, webElement=None):
        super(Element, self).__init__(by_locator, webElement)