# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from nzme_skynet.core.controls.enums.timeouts import DefaultTimeouts
from nzme_skynet.core.driver.driverregistry import DriverRegistry
from nzme_skynet.core.controls import highlight_state
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import time
import logging
from nzme_skynet.core.utils.log import Logger
from typing import Union


Logger.configure_logging()
logger = logging.getLogger(__name__)


class BaseElement(object):
    """
    A base web or mobile element, a wrapper to the selenium/appium element

    :type by: selenium.webdriver.common.by.BY or appium.webdriver.common.mobileby.MobileBy
    :type locator: str
    :type parent: (selenium.webdriver.common.by.BY or appium.webdriver.common.mobileby.MobileBy, str) or
                selenium.webdriver.remote.webelement.WebElement or nzme_skynet.core.controls.baseelement.BaseElement
    """
    def __init__(self, by, locator, parent=None, index=None):
        self._by = by
        self._locator = locator
        self._parent = parent  # The parent element to find the locator in
        self._index = index

    @property
    def element(self):
        """
        Return selenium WebElement
        :return: selenium.webdriver.remote.webelement.WebElement or appium.webdriver.webelement.WebElement
        """
        return self._find_element()

    def _explicitly_find_elements(self, element):
        """
        Find all matching WebElements on the page
        :param element: (selenium.webdriver.common.by.BY or appium.webdriver.common.mobileby.MobileBy, str)
        :return: List of matching WebElements
        """
        try:
            return WebDriverWait(self.driver, DefaultTimeouts.DEFAULT_TIMEOUT).\
                until(ec.presence_of_all_elements_located(element))
        except (TimeoutException, NoSuchElementException) as exception:
            msg = "Timeout: Failed to find element {0}".format(element)
            logger.exception(msg)
            exception.msg += "{}".format(msg)
            raise exception

    def _find_elements(self, element):
        """
        Return matching WebElement/s
        :param element: can be WebElement, BaseElement or a tuple (by, locator)
        :return: WebElement
        """
        if isinstance(element, WebElement):
            elem = WebElement
        elif isinstance(element, BaseElement):
            elem = element.element
        elif isinstance(element, tuple):
            elem = self._explicitly_find_elements(element)
        else:
            elem = None
        return elem

    def _find_element(self):
        """
        Find matching WebElement using locator
        :return: WebElement/s
        """
        if self._parent:
            # Get the parent element (always the first one)
            parent_elem = self._find_elements(self._parent)[0] if isinstance(self._find_elements(self._parent), list) \
                else self._find_elements(self._parent)
            # Find element/s matching within the parent container
            elem = parent_elem.find_elements(self._by, self._locator)[self._index - 1] if self._index \
                else parent_elem.find_element(self._by, self._locator)
        else:
            # Find element/s matching the locator
            a = self._find_elements((self._by, self._locator))
            elem = self._find_elements((self._by, self._locator))[self._index - 1] if self._index \
                else self._find_elements((self._by, self._locator))[0]
        return elem

    def find_sub_elements(self, by, locator):
        # TODO: return list of BaseElement objects
        return self._find_element().find_elements(by, locator)

    @property
    def parent(self):
        # type: () -> WebElement
        # TODO: return  BaseElement object
        return self._find_element().find_element(By.XPATH, "..")

    @property
    def driver(self):
        # type: () -> Union[WebDriver, None]
        """
        Get the underlying selenium/appium webdriver
        :return:
        """
        return DriverRegistry.get_webdriver()

    @property
    def location(self):
        return self._find_element().location

    @property
    def tag_name(self):
        return self._find_element().tag_name

    @property
    def size(self):
        return self._find_element().size

    def exists(self):
        """
        Find the presence of element in the DOM
        :return: True or False
        """
        try:
            self._find_element()
            return True
        except Exception:
            logger.debug(
                "Element {0} is not present in the DOM".format(self._locator))
            return False

    def _highlight(self):
        """
        Highlight the element being interacted if was requested during driver initialisation
        :return: None
        """
        if highlight_state():
            elem = self._find_element()

            def apply_style(style):
                self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                           elem, style)
            previous_style = self.get_attribute('style')
            apply_style("background: yellow; border: 2px solid red;")
            time.sleep(0.3)
            apply_style(previous_style)

    def get_attribute(self, attribute):
        return self._find_element().get_attribute(attribute)

    def has_attribute(self, attribute):
        try:
            return self.get_attribute(attribute)
        except Exception:
            logger.debug("Element {0} does not have attribute {1}".format(
                self._locator, attribute))
            return False

    def get_css_property(self, css_property):
        return self._find_element().value_of_css_property(css_property)

    def scroll_to_element(self, offset=200):
        """
        Scroll to the element
        :param offset:
        :return: None
        """
        self.driver.execute_script(
            "window.scrollBy(0," + str(self.location['y'] - offset) + ");")

    def scroll_into_view(self):
        """
        Scroll element into viewport
        :return: None
        """
        self._find_element().location_once_scrolled_into_view()

    # Visibility, Presence, Clickability

    def is_currently_visible(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        # type: (int) -> Union[WebElement, bool]
        """
        Finds if the element is visible within 1 sec (default) and returns the element.
        Should be used to check visibility of an element on a page that has already loaded.
        :param time: explicit time to wait for, default 1sec
        :return: WebElement if True or False
        """
        return self.will_be_visible(time=time)

    def will_be_visible(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        # type: (int) -> Union[WebElement, bool]
        """
        Finds if the element is visible within 10 sec (default) and returns the element.
        Can be used to check visibility of an element e.g. when waiting for a page to load.
        :param time: explicit time to wait for, default 10secs
        :return: WebElement if True or False
        """
        try:
            return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((self._by, self._locator)))
        except Exception:
            logger.debug("Element {0} was not visible in time {1} secs".format(
                self._locator, str(time)))
            return False

    def is_currently_present(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        # type: (int) -> Union[WebElement, bool]
        """
        Finds if the element is present in the DOM within 1 sec (default) and returns the element.
        Should be used to check presence of an element on a page that has already loaded.
        :param time: explicit time to wait for, default 1sec
        :return: WebElement if True or False
        """
        return self.will_be_present(time=time)

    def will_be_present(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        # type: (int) -> Union[WebElement, bool]
        """
        Finds if the element is present in the DOM within 10 sec (default) and returns the element.
        Should be used to check visibility of an element e.g. when waiting for a page to load.
        :param time: explicit time to wait for, default 10secs
        :return: WebElement if True or False
        """
        try:
            return WebDriverWait(self.driver, time).until(ec.presence_of_element_located((self._by, self._locator)))
        except Exception:
            logger.debug("Element {0} was not present in time {1} secs".format(
                self._locator, time))
            return False

    def is_not_displayed(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        # type: (int) -> Union[WebElement, bool]
        """
        Finds if the element is not displaying within 1 sec (default).
        Should be used to check absence of an element on a page that has already loaded.
        :param time: explicit time to wait for, default 1sec
        :return: True or False
        """
        return self.will_not_be_displayed(time=time)

    def will_not_be_displayed(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        # type: (int) -> Union[WebElement, bool]
        """
        Finds if the element is not displaying within 10 sec (default).
        Should be used to check visibility of an element e.g. when waiting for a page to load.
        :param time: explicit time to wait for, default 10secs
        :return: True or False
        """
        try:
            return WebDriverWait(self.driver, time).until(ec.invisibility_of_element_located((self._by, self._locator)))
        except Exception:
            logger.debug("Element {0} was not invisible in time {1} secs".format(
                self._locator, time))
            return False

    def is_ready_to_interact(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        # type: (int) -> Union[WebElement, bool]
        """
        Finds if the element is present, displaying and ready to interact within 1 sec (default).
        Should be used to check interaction of an element on a page that has already loaded.
        :param time: explicit time to wait for, default 1sec
        :return: WebElement if True or False
        """
        return self.will_be_ready_to_interact(time=time)

    def will_be_ready_to_interact(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        # type: (int) -> Union[WebElement, bool]
        """
        Finds if the element is present, displaying and ready to interact within 10 sec (default).
        Should be used to check interaction of an element e.g. when waiting for a page to load.
        :param time: explicit time to wait for, default 10secs
        :return: WebElement if True or False
        """
        try:
            return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable((self._by, self._locator)))
        except Exception:
            logger.debug("Element {0} was not clickable in time {1} secs".format(
                self._locator, time))
            return False

    def hover_over(self):
        """
        Hover the mouse over the element
        :return: None
        """
        hover = ActionChains(self.driver).move_to_element(self._find_element())
        hover.perform()

    def focus(self):
        """
        Hover and focus on the element
        :return: None
        """
        hover = ActionChains(self.driver).move_to_element(self._find_element())
        hover.click()
        hover.perform()
