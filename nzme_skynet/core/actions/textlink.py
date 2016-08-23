# coding=utf-8
from nzme_skynet.core.actions.component import Component


class TextLink(Component):
    def __index__(self, by_locator):
        super(TextLink, self).__init__(by_locator)

    def getHref(self):
        pass
