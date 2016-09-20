# coding=utf-8
from selenium.webdriver.common.by import By

from nzme_skynet.core.actions.controls.component import Component

class Table(Component):
    def __init__(self, driver, locator, by=By.CSS_SELECTOR):
        super(Table, self).__init__(driver, locator, by)
