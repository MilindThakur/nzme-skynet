# coding=utf-8
from nzme_skynet.core.controls.clickabletext import ClickableText


class Button(ClickableText):
    """

    """
    def __init__(self, by, locator):
        super(Button, self).__init__(by, locator)

    def get_status(self):
        """
        Validates the DOM for the element, highlights when the element is present and
        gets the attribute/value of the element.
        :return:
        """
        self._highlight()
        self.get_attribute("value")
