# coding=utf-8
import time

from nzme_skynet.core.controls.clickable import Clickable
from nzme_skynet.core.controls.enums.timeouts import DefaultTimeouts
import logging
from nzme_skynet.core.utils.log import Logger

Logger.configure_logging()
logger = logging.getLogger(__name__)

class Image(Clickable):
    """
    This class extends Clickable class and contains actionable properties with Images

    :param by: type of locator
    :param locator: locator value
    """

    def __init__(self, by, locator):
        super(Image, self).__init__(by, locator)

    @property
    def src(self):
        """
        This method validates the DOM for the visibility of the element, highlights when the element is visible.
        Returns the src when present and False when the element is not visible.

        :return: attributeValue or False
        """
        self._highlight()
        return self.get_attribute("src")

    def get_filename(self):
        raise NotImplementedError

    def is_image_loaded(self):
        """
        This method synchronously executes the JavaScript to find if the element is present and returns the web element
        if natural width is undefined and greater than 0. Returns False with a debug message when the element is not
        present.

        :return: element or False
        """
        try:
            return self.driver.execute_script("return arguments[0].complete && "
                                              "typeof arguments[0].naturalWidth != \"undefined\" && "
                                              "arguments[0].naturalWidth > 0", self._find_element())
        except Exception as e:
            logger.debug("Element {0} is not present in the DOM".format(self._locator))
            return False

    def _wait_for_lazy_loaded_image(self, timeout=DefaultTimeouts.DEFAULT_TIMEOUT):
        """
        This method will enable the driver to wait and poll for 5 seconds to validate if data-original is equal to
        src value and returns True if they are equal. Returns False on failing within 5 seconds.

        :param timeout: DEFAULT_TIMEOUT of 5 seconds
        :return: boolean
        """
        start_ms = time.time() * 1000.0
        stop_ms = start_ms + (timeout * 1000.0)
        for x in range(int(timeout * 10)):
            if self.get_attribute('data-original') == self.get_attribute('src'):
                return True
            else:
                now_ms = time.time() * 1000.0
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
        return False

    def wait_for_image_to_load(self, lazy_loading=False, timeout=DefaultTimeouts.DEFAULT_TIMEOUT):
        """
        This method will invoke _wait_for_lazy_loaded_image method when the lazy_loading parameter is True.
        And will invoke will_be_visible when the lazy_loading parameter is False. In either case, this method will
        return a boolean value depending on the visibility of the element.

        :param lazy_loading: boolean
        :param timeout: DEFAULT_TIMEOUT of 5 seconds
        :return: boolean
        """
        if lazy_loading:
            return self._wait_for_lazy_loaded_image(timeout)
        else:
            return self.will_be_visible()

    @property
    def title(self):
        """
        This method validates DOM for visibility of the element, highlights when the element is visible.
        Returns the title of the element when present and False when the element is not visible.

        :return: attributeValue or False
        """
        self._highlight()
        return self.get_attribute("title")

    @property
    def width(self):
        """
        This method validates the DOM for the visibility of the element, highlights when the element is visible.
        Returns the width of the element when present and False when the element is not visible.

        :return: attributeValue or False
        """
        self._highlight()
        return self.get_attribute("width")

    @property
    def height(self):
        """
        This method validates the DOM for the visibility of the element, highlights when the element is visible.
        Returns the height of the element when present and False when the element is not visible.

        :return: attributeValue or False
        """
        self._highlight()
        return self.get_attribute("height")
