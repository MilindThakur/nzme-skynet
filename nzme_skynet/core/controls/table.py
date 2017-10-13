# coding=utf-8
from selenium.webdriver.common.by import By

from nzme_skynet.core.controls.baseelement import BaseElement


class Table(BaseElement):

    def __init__(self, locator, by=By.CSS_SELECTOR):
        super(Table, self).__init__(locator, by)
