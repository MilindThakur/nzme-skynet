# coding=utf-8
from nzme_skynet.core.controls.clickabletext import ClickableText


class Button(ClickableText):

    def get_status(self):
        self._highlight()
        self.get_attribute("value")

    @property
    def text(self):
        """
        Return the txt of button,  if "input" element return value
        otherwise return inner text.
        """
        self._highlight()
        if self.tag_name == "input":
            return self.get_attribute("value")
        else:
            return self._find_element().text
