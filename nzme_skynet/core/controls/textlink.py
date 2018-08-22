# coding=utf-8
from nzme_skynet.core.controls.clickabletext import ClickableText


class TextLink(ClickableText):

    def __init_(self, by, locator):
        super(TextLink, self).__init__(by, locator)

    @property
    def href(self):
        """
        Validates the DOM for the tooltip, highlights when the tooltip is present and
        gets/ returns the attribute/href of the element.
        :return:
        """
        self._highlight()
        return self.get_attribute("href")

    @property
    def tootltip(self):
        """
        Validates the DOM for the tooltip, highlights when the tooltip is present and
        gets/ returns the attribute/title of the element.
        :return:
        """
        self._highlight()
        return self.get_attribute('title')
