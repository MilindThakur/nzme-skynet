# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component

from selenium.webdriver.common.by import By

class TextLink(Component):
    def __index__(self, driver, locator, by=By.CSS_SELECTOR):
        super(TextLink, self).__init__(driver, locator, by)

    def get_href(self):
        self.get_attr("href")
