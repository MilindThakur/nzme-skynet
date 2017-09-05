# coding=utf-8
from distutils.util import strtobool
from nzme_skynet.core.actions.controls.component import Component


class MobElem(Component):
    def __init__(self, driver, locator, by):
        super(MobElem, self).__init__(driver, locator, by)

    def click(self):
        if self.will_be_visible():
            self.driver.find_element(by=self.by, value=self.locator).click()

    def get_text(self):
        return self.get_attr("text")

    def set_text(self,text):
        self.clear_text()
        return self.driver.find_element(by=self.by, value=self.locator).set_text(text)

    def clear_text(self):
        return self.driver.find_element(by=self.by, value=self.locator).set_text("")

    def get_class(self):
        return self.get_attr("class")

    def get_package(self):
        return self.get_attr("package")

    def get_content_desc(self):
        return self.get_attr("content-desc")

    def is_checkable(self):
        return strtobool(self.get_attr("checkeable"))

    def is_checked(self):
        return strtobool(self.get_attr("checked"))

    def is_clickable(self):
        return strtobool(self.get_attr("clickable"))

    def is_long_clickable(self):
        return strtobool(self.get_attr("long-clickable"))

    def is_focused(self):
        return strtobool(self.get_attr("focused"))

    def is_focusable(self):
        return strtobool(self.get_attr("focusable"))

    def is_scrollable(self):
        return strtobool(self.get_attr("scrollable"))

    def is_password(self):
        return strtobool(self.get_attr("password"))

    def is_selected(self):
        return strtobool(self.get_attr("selected"))

    #
    # def get_location(self):
    #     self.X = self.get_attr("bounds")
    #     self.Y =
