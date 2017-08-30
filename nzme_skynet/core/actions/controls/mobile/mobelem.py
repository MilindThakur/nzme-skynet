# coding=utf-8
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.mobileby import By
from nzme_skynet.core.actions.controls.component import Component


class MobElem(Component):
    def __init__(self, driver, locator, by):
        super(MobElem, self).__init__(driver, locator, by)

    def click(self):
        if self.will_be_visible():
            self.driver.find_element(by=self.by, value=self.locator).click()

    def get_text(self):
        return str(self.get_attr("text"))

    def set_text(self,text):
        self.clear_text()
        return self.driver.find_element(by=self.by, value=self.locator).set_text(text)

    def clear_text(self):
        return self.driver.find_element(by=self.by, value=self.locator).set_text("")

    def get_class(self):
        return str(self.get_attr("class"))

    def get_package(self):
        return str(self.get_attr("package"))

    def get_content_desc(self):
        return str(self.get_attr("content-desc"))

    def is_checkable(self):
        if str(self.get_attr("checkeable")) == 'false':
            return False
        else:
            return True

    def is_checked(self):
        if str(self.get_attr("checked")) == 'false':
            return False
        else:
            return True

    def is_clickable(self):
        if str(self.get_attr("clickable")) == 'false':
            return False
        else:
            return True

    def is_long_clickable(self):
        if str(self.get_attr("long-clickable")) == 'false':
            return False
        else:
            return True

    def is_focused(self):
        if str(self.get_attr("focused")) == 'false':
            return False
        else:
            return True

    def is_focusable(self):
        if str(self.get_attr("focusable")) == 'false':
            return False
        else:
            return True

    def is_scrollable(self):
        if str(self.get_attr("scrollable")) == 'false':
            return False
        else:
            return True

    def is_password(self):
        if str(self.get_attr("password")) == 'false':
            return False
        else:
            return True

    def is_selected(self):
        if str(self.get_attr("selected")) == 'false':
            return False
        else:
            return True
    #
    # def get_location(self):
    #     self.X = self.get_attr("bounds")
    #     self.Y =
