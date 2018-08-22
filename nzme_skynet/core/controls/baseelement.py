# -*- coding: utf-8 -*-
from nzme_skynet.core.controls.enums.timeouts import DefaultTimeouts
from nzme_skynet.core.driver.driverregistry import DriverRegistry
from nzme_skynet.core.controls import highlight_state
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging
from nzme_skynet.core.utils.log import Logger


Logger.configure_logging()
logger = logging.getLogger(__name__)


class BaseElement(object):
    def __init__(self, by, locator):
        self._by = by
        self._locator = locator

    def _find_element(self):
        """
        An expectation for checking that an element is present on the DOM
        of a page with a conditional wait.
        _locator - used to find the element with locator value
        _by - type of locator
        Returns the web element once it is located
        :return:
        """
        try:
            return WebDriverWait(self.driver, DefaultTimeouts.DEFAULT_TIMEOUT).until(ec.presence_of_element_located((self._by, self._locator)))
        except Exception as e:
            logger.exception("Timeout: Failed to find element {0}".format(self._locator))
            raise

    def find_sub_elements(self, by, locator):
        """
        TODO: return list of Element objects
        Find elements given a By strategy and locator. Prefer the find_elements_by_* methods when
        possible.

        :rtype: list of WebElement
        :param by: type of locator
        :param locator: used to find the element with locator value
        Returns the list of Element objects
        :return:
        """
        return self._find_element().find_elements(by, locator)

    @property
    def driver(self):
        """
        Returns Selenium Webdriver from registry
        :return:
        """
        return DriverRegistry.get_webdriver()

    @property
    def location(self):
        """
        Returns the location of the web element in the renderable canvas.
        :return:
        """
        return self._find_element().location

    @property
    def size(self):
        """
        Returns the size of the web element.
        :return:
        """
        return self._find_element().size

    def exists(self):
        """
        Check if the web element exists in the DOM using ._find_element function
        Returns true on successful existence of the element and false on failure
        :return:
        """
        try:
            self._find_element()
            return True
        except Exception as e:
            logger.debug("Element {0} is not present in the DOM".format(self._locator))
            return False

    def _highlight(self):
        """
        An expectation for checking that an element is present on the DOM of a
        page and synchronously executes the javascript to highlight the element that is visible
        :return:
        """
        if highlight_state():
            elem = self.will_be_visible()

            def apply_style(style):
                self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                           elem, style)
            previous_style = self.get_attribute('style')
            apply_style("background: yellow; border: 2px solid red;")
            time.sleep(0.3)
            apply_style(previous_style)

    def get_attribute(self, attribute):
        """
        Gets the given attribute or property of the element.

        This method will first try to return the value of a property with the
        given name. If a property with that name doesn't exist, it returns the
        value of the attribute with the same name. If there's no attribute with
        that name, ``None`` is returned.

        :param attribute: Name of the attribute/property to retrieve.
        :return:
        """
        return self._find_element().get_attribute(attribute)

    def has_attribute(self, attribute):
        """
        Returns the attribute or property of the element if the element is present
        otherwise, returns False
        :param attribute: Name of the attribute/property to retrieve.
        :return:
        """
        try:
            return self.get_attribute(attribute)
        except Exception:
            logger.debug("Element {0} does not have attribute {1}".format(self._locator, attribute))
            return False

    def get_css_property(self, css_property):
        """
        Gets the value of a CSS property
        :param css_property: property name
        :return:
        """
        return self._find_element().value_of_css_property(css_property)

    def scroll_to_element(self, offset=200):
        """
         Synchronously Executes JavaScript to scroll to the element in the current window/frame.
        :return:
        """
        self.driver.execute_script("window.scrollBy(0," + str(self.location['y'] - offset) + ");")

    # Visibility, Presence, Clickability

    def is_currently_visible(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        """
         An expectation for checking that an element is present on the DOM of a
         page and visible. Visibility means that the element is not only displayed
         but also has a height and width that is greater than 0.
         returns the WebElement once it is located and visible
         :param time: time that the driver would wait
         :return:
         """
        return self.will_be_visible(time=time)

    def will_be_visible(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        """
        An expectation for checking that an element is present on the DOM of a
        page and visible. Visibility means that the element is not only displayed
        but also has a height and width that is greater than 0.
        returns the WebElement once it is located and visible
        :param time: time that the driver would wait
        :return:
        """
        try:
            return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((self._by, self._locator)))
        except Exception:
            logger.debug("Element {0} was not visible in time {1} secs".format(self._locator, str(time)))
            return False

    def is_currently_present(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        """
        An expectation for checking that an element is present on the DOM
        of a page. This does not necessarily mean that the element is visible.
        returns the WebElement once it is located
        :param time: time that the driver would wait
        :return:
        """
        return self.will_be_present(time=time)

    def will_be_present(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        """
        An expectation for checking that an element is present on the DOM
        of a page. This does not necessarily mean that the element is visible.
        returns the WebElement once it is located
        :param time: time that the driver would wait
        :return:
        """
        try:
            return WebDriverWait(self.driver, time).until(ec.presence_of_element_located((self._by, self._locator)))
        except Exception:
            logger.debug("Element {0} was not present in time {1} secs".format(self._locator, time))
            return False

    def is_not_displayed(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        """
        An Expectation for checking that an element is either invisible or not
        present on the DOM.
        :param time: time that the driver would wait
        :return:
        """
        return self.will_not_be_displayed(time=time)

    def will_not_be_displayed(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        """
        An Expectation for checking that an element is either invisible or not
        present on the DOM.
        :param time: time that the driver would wait
        :return:
        """
        try:
            return WebDriverWait(self.driver, time).until(ec.invisibility_of_element_located((self._by, self._locator)))
        except Exception:
            logger.debug("Element {0} was not invisible in time {1} secs".format(self._locator, time))
            return False

    def is_ready_to_interact(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        """
        An Expectation for checking an element is visible and enabled within a wait time such that
        you can click it.
        :param time: time that the driver would wait
        Returns the web element
        :return:
        """
        return self.will_be_ready_to_interact(time=time)

    def will_be_ready_to_interact(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        """
        An Expectation for checking an element is visible and enabled within a wait time such that
        you can click it.
        :param time: time that the driver would wait
        Returns the web element
        :return:
        """
        try:
            return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable((self._by, self._locator)))
        except Exception:
            logger.debug("Element {0} was not clickable in time {1} secs".format(self._locator, time))
            return False

    def hover_over(self):
        """
        This method helps in performing mouse hover over action using ActionChains, move_to_element and perform methods
        :return:
        """
        hover = ActionChains(self.driver).move_to_element(self._find_element())
        hover.perform()

    def focus(self):
        """
        TODO: Implement focus function
        :return:
        """
        raise NotImplementedError
