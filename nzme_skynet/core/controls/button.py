# coding=utf-8
from nzme_skynet.core.controls.clickabletext import ClickableText


class Button(ClickableText):
    """
    This class extends ClickableText class and contains method to retrieve the the status of the button

    :param by: type of locator
    :param locator: locator value

    Usage Example::

        login_button = Button(By.ID, "uniqueID")

        login_button.get_status()
        button_text = login_button.text
        login_button.click()
        login_button.hover_over()
        login_button.is_ready_to_interact()

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
