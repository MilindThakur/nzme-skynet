# coding=utf-8
from nzme_skynet.core.controls.clickabletext import ClickableText


class TextLink(ClickableText):

    @property
    def href(self):
        self._highlight()
        return self.get_attribute("href")

    @property
    def tootltip(self):
        self._highlight()
        return self.get_attribute('title')
