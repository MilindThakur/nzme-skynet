# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component

from selenium.webdriver.common.by import By

class TextInput(Component):
    def __init__(self, driver, locator, by=By.CSS_SELECTOR):
        super(TextInput, self).__init__(driver, locator, by)

    def get_value(self):
        return self.get_attribute("value")

    def clear(self):
        super(TextInput, self).clear()
