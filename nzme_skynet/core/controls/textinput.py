# coding=utf-8
from nzme_skynet.core.controls.text import Text


class TextInput(Text):

    def __init__(self, by, locator):
        super(TextInput, self).__init__(by, locator)

    def clear(self):
        self._highlight()
        self.focus()
        self._find_element().clear()

    @property
    def value(self):
        self._highlight()
        return self.get_attribute("value")

    def set_value(self, value):
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
