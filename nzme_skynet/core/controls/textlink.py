# coding=utf-8
from nzme_skynet.core.controls.clickabletext import ClickableText


class TextLink(ClickableText):
    """
    This class extends ClickableText class and contains methods to return href, title value of the element

    :param by: type of locator
    :param locator: locator value
    """

    def __init_(self, by, locator):
        super(TextLink, self).__init__(by, locator)

    @property
    def href(self):
        """
        This method validates DOM for visibility of the element, highlights the same when present and
        returns the attribute/href of the element.

        :return: href or False
        """
        self._highlight()
        return self.get_attribute("href")

    @property
    def tootltip(self):
        """
        This method validates DOM for visibility of the element, highlights the same when present and
        returns the attribute/title of the element.

        :return: title or False
        """
        self._highlight()
        return self.get_attribute('title')
