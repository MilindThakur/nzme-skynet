# coding=utf-8
from nzme_skynet.core.controls.clickabletext import ClickableText


class Button(ClickableText):
    """
    This class extends ClickableText class and contains method to retrieve the the status of the element

    :param by: type of locator
    :param locator: locator value
    """
    def __init__(self, by, locator):
        super(Button, self).__init__(by, locator)

    def get_status(self):
        """
        This method validates the DOM for the visibility of the element, highlights when the element is present and
        gets the attribute/value of the element.

        :return:attributeValue or False
        """
        self._highlight()
        self.get_attribute("value")
