# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException
import logging
from nzme_skynet.core.controls.baseelement import BaseElement
from selenium.webdriver.common.action_chains import ActionChains
logger = logging.getLogger(__name__)


class Clickable(BaseElement):

    def __init__(self, by, locator):
        super(Clickable, self).__init__(by, locator)

    def click(self):
        original_url = self.driver.current_url
        elem = self.is_ready_to_interact()
        if elem:
            self._highlight()
            try:
                elem.click()
                return
            except Exception as e:
                logger.debug("Failed to click elem {0}. Exception: {1}".format(self._locator, e.message))
                if self.driver.current_url == original_url:
                    logger.debug("Currently on the same page, trying other click options..")
                    try:
                        logger.debug("Trying click using JS...")
                        self.driver.execute_script("arguments[0].click();", elem)
                        return
                    except Exception as e:
                        logger.debug("Failed JS click. Exception: {0}".format(e.message))
                        try:
                            logger.debug("Trying click using Action chain..")
                            hover = ActionChains(self.driver).move_to_element(elem)
                            hover.click()
                            hover.perform()
                            return
                        except Exception as e:
                            logger.exception("Failed all ways to click on element, raising exception. Exception: {0}"
                                             .format(e.message))
                            raise
                else:
                    logger.debug("The page has already transitioned to a new page, stopping click method")
                    return
        logger.exception("Element {0} is not available to interact with".format(self._locator))
        raise Exception("Element {0} is not available to interact with".format(self._locator))

    def clickjs(self):
        self.driver.execute_script("arguments[0].click();", self._find_element())

    def _scroll_and_click(self):
        self.scroll_to_element()
        self.click()

    def click_parent(self):
        self._find_element().find_element_by_xpath('..').click()
