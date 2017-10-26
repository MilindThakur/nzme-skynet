# coding=utf-8
from nzme_skynet.core.controls.clickabletext import ClickableText


class TextLink(ClickableText):

    def __init_(self, by, locator):
        super(TextLink, self).__init__(by, locator)

    @property
    def href(self):
        return self.get_attribute("href")

    @property
    def tootltip(self):
        return self.get_attribute('title')
