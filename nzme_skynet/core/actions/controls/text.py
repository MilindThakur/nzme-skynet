# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component

from selenium.webdriver.common.by import By

class Text(Component):
    def __init__(self, driver, locator, by=By.CSS_SELECTOR):
        super(Text, self).__init__(driver, locator, by)

    def get_text(self):
        return super(Text, self).get_text()

    def text_contains(self, text):
        return self.get_text().contains(text)

    def text_matches(self, regex):
        return self.get_text().matches(regex)
