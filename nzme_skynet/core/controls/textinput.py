# coding=utf-8
from nzme_skynet.core.controls.text import Text


class TextInput(Text):

    def __init__(self, by, locator):
        super(TextInput, self).__init__(by, locator)

    def clear(self):
        """
        An expectation for checking that an element is present on the DOM of a
        page. Clears any pre existing text.
        :return:
        """
        self._highlight()
        self._find_element().clear()

    @property
    def value(self):
        """
        An expectation for checking that an element is present on the DOM of a
        page and gets the attribute/value of the element.
        :return:
        """
        self._highlight()
        return self.get_attribute("value")

    def set_value(self, value):
        """
        An expectation for checking that an element is present on the DOM of a
        page and visible. Clears any pre existing text and inputs the value to the TextInput field.
        :param value: input value to the web element
        :return:
        """
        self.is_currently_visible()
        self.clear()
        self._find_element().send_keys(value)
