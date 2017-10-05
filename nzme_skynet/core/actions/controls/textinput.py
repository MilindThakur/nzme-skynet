# coding=utf-8

from selenium.webdriver.common.by import By

from nzme_skynet.core.actions.controls.text import Text


class TextInput(Text):

    def __init__(self, driver, locator, by=By.CSS_SELECTOR):
        super(TextInput, self).__init__(driver, locator, by)

    def focus(self):
        raise NotImplementedError

    def clear(self):
        self.find_element().clear()

    def get_value(self):
        return self.get_attr("value")

    def set_value(self, value):
        self.clear()
        self.find_element().send_keys(value)
