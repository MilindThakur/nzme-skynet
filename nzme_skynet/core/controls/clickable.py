# -*- coding: utf-8 -*-
from nzme_skynet.core.controls.baseelement import BaseElement


class Clickable(BaseElement):

    def __init__(self, by, locator):
        super(Clickable, self).__init__(by, locator)

    def click(self):
        self.is_ready_to_interact()
        self._highlight()
        self._find_element().click()

    def clickjs(self):
        self.driver.execute_script("arguments[0].click();", self._find_element())

    def scroll_and_click(self):
        self.scroll_to_element()
        self.click()

    def click_parent(self):
        self._find_element().find_element_by_xpath('..').click()
