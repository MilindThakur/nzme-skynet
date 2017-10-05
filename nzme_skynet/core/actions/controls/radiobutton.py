# coding=utf-8
from selenium.webdriver.common.by import By

from nzme_skynet.core.actions.controls.button import Button


class RadioButton(Button):
    def __init__(self, driver, locator, by=By.CSS_SELECTOR):
        super(RadioButton, self).__init__(driver, locator, by)
