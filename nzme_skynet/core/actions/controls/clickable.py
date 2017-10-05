# -*- coding: utf-8 -*-
from nzme_skynet.core.actions.controls.component import Component


class Clickable(Component):

    def __init__(self, driver, locator, by):
        super(Clickable, self).__init__(driver, locator, by)

    def click(self):
        self.is_ready_to_interact()
        self.find_element().click()

    def clickjs(self):
        self._driver.execute_script("arguments[0].click();", self.find_element())

    def scroll_and_click(self):
        self.scroll_to_element()
        self.click()
