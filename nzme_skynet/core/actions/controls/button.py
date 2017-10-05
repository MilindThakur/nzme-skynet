# coding=utf-8
from selenium.webdriver.common.by import By

from nzme_skynet.core.actions.controls.clickabletext import ClickableText


class Button(ClickableText):

    def __init__(self, driver, locator, by=By.CSS_SELECTOR):
        super(Button, self).__init__(driver, locator, by)

    def get_status(self):
        self.get_attr("value")
