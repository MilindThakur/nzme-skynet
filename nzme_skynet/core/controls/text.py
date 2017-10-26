# coding=utf-8
from nzme_skynet.core.controls.clickabletext import ClickableText


class Text(ClickableText):

    def __init__(self, by, locator):
        super(Text, self).__init__(by, locator)
