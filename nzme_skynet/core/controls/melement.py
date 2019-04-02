# coding=utf-8
from distutils.util import strtobool
from nzme_skynet.core.controls.baseelement import BaseElement


class MElement(BaseElement):

    def click(self):
        self.is_ready_to_interact()
        # Highlight here, This needs to be implemented for mobile
        self._find_element().click()

    @property
    def text(self):
        return self.get_attribute("text")

    def set_text(self, text):
        self.clear_text()
        return self._find_element().set_text(text)

    def clear_text(self):
        return self._find_element().set_text("")

    @property
    def classname(self):
        return self.get_attribute("class")

    @property
    def package(self):
        return self.get_attribute("package")

    @property
    def content_desc(self):
        return self.get_attribute("content-desc")

    def is_checkable(self):
        return strtobool(self.get_attribute("checkeable"))

    def is_checked(self):
        return strtobool(self.get_attribute("checked"))

    def is_clickable(self):
        return strtobool(self.get_attribute("clickable"))

    def is_long_clickable(self):
        return strtobool(self.get_attribute("long-clickable"))

    def is_focused(self):
        return strtobool(self.get_attribute("focused"))

    def is_focusable(self):
        return strtobool(self.get_attribute("focusable"))

    def is_scrollable(self):
        return strtobool(self.get_attribute("scrollable"))

    def is_password(self):
        return strtobool(self.get_attribute("password"))

    def is_selected(self):
        return strtobool(self.get_attribute("selected"))
