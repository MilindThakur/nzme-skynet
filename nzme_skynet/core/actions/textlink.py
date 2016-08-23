# coding=utf-8

class TextLink(object):
    def __index__(self, by_locator):
        self.locator = by_locator

    def getHref(self):
        pass