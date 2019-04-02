# coding=utf-8
from nzme_skynet.core.controls.text import Text


class TextInput(Text):

    def clear(self):
        """
        Clear the Text input field
        """
        self._highlight()
        self.focus()
        self._find_element().clear()

    @property
    def value(self):
        """
        Returns value of the Text field
        :return:
        """
        self._highlight()
        return self.get_attribute("value")

    def set_value(self, value):
        """
        Clear Text input field and set a new value
        :param value:
        :return:
        """
        self.is_currently_visible()
        self.clear()
        self._find_element().send_keys(value)

    def update_value(self, new_value):
        """
        Completely updates the exiting text value to a new value specified
        :param new_value: the new value to update
        """
        # Check if text element is visible
        # Clear existing value
        # Set new value
        raise NotImplemented
