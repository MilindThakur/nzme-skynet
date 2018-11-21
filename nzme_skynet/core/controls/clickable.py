# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException
import logging
from nzme_skynet.core.controls.baseelement import BaseElement
import logging
from nzme_skynet.core.utils.log import Logger
from selenium.webdriver.common.action_chains import ActionChains

Logger.configure_logging()
logger = logging.getLogger(__name__)


class Clickable(BaseElement):
    """
    This class extends BaseElement class and contains methods that help in
    performing different type of click actions by utilising the properties defined in BaseClass

    :param by: type of locator
    :param locator: locator value
    """

    def __init__(self, by, locator):
        super(Clickable, self).__init__(by, locator)

    def dblclick(self):
        """
        Double clicks an element.

        Usage Example:

            elem = Clickable(By.ID, "uniqueID")
            elem.dblclick()

        """
        raise NotImplementedError

    def click(self):
        """
        Allows a click on an element. This command will try performing different clicks before throwing exception.
        It will:

         - Check if element is ready to interact with and then click
         - If fails, tries JS click
         - If fails, tries mouse click
         - Else throw exception

        """
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
        """
        This method synchronously executes the JavaScript to perform click action when the element is present and
        returns False with a debug log when the element is not present.
        action

        :return: perform click action or False
        """
        try:
            self.driver.execute_script("arguments[0].click();", self._find_element())
        except Exception as e:
            logger.debug("Element {0} is not present in the DOM".format(self._locator))
            return False

    def scroll_and_click(self):
        """
        This method invokes the JavaScript to scroll to the element and then perform click action when the element is
        present. Returns False with a debug log when the element is not present.

        :return: perform click action or False
        """
        try:
            self.scroll_to_element()
            self.click()
        except Exception as e:
            logger.debug("Element {0} is not present in the DOM".format(self._locator))
            return False

    def click_parent(self):
        self._find_element().find_element_by_xpath('..').click()
