# coding=utf-8
from nzme_skynet.core.controls.text import Text


class TextInput(Text):
    """
    This class extends Text class and contains methods that help in performing different action with TextInput

    :param by: type of locator
    :param locator: locator value
    """

    def __init__(self, by, locator):
        super(TextInput, self).__init__(by, locator)

    def clear(self):
        """
        This method validates DOM for visibility of the element, highlights the same when present
        and clears any pre existing text.

        :return: clear or False
        """
        self._highlight()
        self._find_element().clear()

    @property
    def value(self):
        """
        This method validates DOM for visibility of the element, highlights the same when present
        and returns the attribute/value of the element.

        :return: value or False
        """
        self._highlight()
        return self.get_attribute("value")

    def set_value(self, value):
        """
        This method validates DOM for visibility of the element.
        Clears any pre existing text and inputs the value to the TextInput field.

        :param value: input value to the web element
        """
        self.is_currently_visible()
        self.clear()
        self._find_element().send_keys(value)
