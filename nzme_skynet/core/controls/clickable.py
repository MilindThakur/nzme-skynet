# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException
import logging
from nzme_skynet.core.controls.baseelement import BaseElement
logger = logging.getLogger(__name__)


class Clickable(BaseElement):

    def __init__(self, by, locator):
        super(Clickable, self).__init__(by, locator)

    def click(self):
        self.is_ready_to_interact()
        self._highlight()
        try:
            self._find_element().click()
        except WebDriverException:
            logger.debug("Failed to click, trying to click using JS executor..")
            try:
                self.clickjs()
            except WebDriverException:
                logger.debug("Failed JS click, trying click using Actions..")
                try:
                    self.scroll_to_element()
                    self.focus()
                except Exception:
                    logger.exception("Failed all ways to click on element, raising exception")
                    raise

    def clickjs(self):
        self.driver.execute_script("arguments[0].click();", self._find_element())

    def _scroll_and_click(self):
        self.scroll_to_element()
        self.click()

    def click_parent(self):
        self._find_element().find_element_by_xpath('..').click()
