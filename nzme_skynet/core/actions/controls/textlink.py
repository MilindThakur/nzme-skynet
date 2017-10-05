# coding=utf-8
from selenium.webdriver.common.by import By

from nzme_skynet.core.actions.controls.clickabletext import ClickableText


class TextLink(ClickableText):

    def __init_(self, driver, locator, by=By.CSS_SELECTOR):
        super(TextLink, self).__init__(driver, locator, by)

    def get_href(self):
        return self.get_attr("href")

    def get_tootltip(self):
        return self.get_attr('title')
