# coding=utf-8
from selenium.webdriver.common.by import By
from nzme_skynet.core.actions.controls.component import Component


class MobElem(Component):
    def __init__(self, driver, locator, by=By.CSS_SELECTOR):
        super(MobElem, self).__init__(driver, locator, by)

    def get_index(self):
        return self.get_attr("index")

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
        return self.get_attr("checkable")

    def is_checked(self):
        if str(self.get_attr("checked")) == 'false':
            return False
        else:
            return True

    def is_clickable(self):
        return self.get_attr("clickable")

    def is_long_clickable(self):
        return self.get_attr("long-clickable")

    def is_enabled(self):
        return self.get_attr("enabled")

    def is_focused(self):
        return self.get_attr("focused")

    def is_focusable(self):
        return self.get_attr("focusable")

    def is_scrollable(self):
        return self.get_attr("scrollable")

    def is_password(self):
        return self.get_attr("password")

    def is_selected(self):
        return self.get_attr("selected")
    #
    # def get_location(self):
    #     self.X = self.get_attr("bounds")
    #     self.Y =
