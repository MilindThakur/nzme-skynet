# coding=utf-8
from nzme_skynet.core.controls.clickabletext import ClickableText


class Button(ClickableText):

    def __init__(self, by, locator):
        super(Button, self).__init__(by, locator)

    def get_status(self):
        self._highlight()
        self.get_attribute("value")
