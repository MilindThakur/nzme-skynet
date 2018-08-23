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
    """
    BaseElement class contains those methods that could be used in conjunction with other other methods in this
    framework or independently.
    This class contains methods that wraps and uses some pre-existing selenium methods/ objects with some additional
    capabilities to make them more user friendly

    :param by: type of locator
    :param locator: locator value
    """
    def __init__(self, by, locator):
        self._by = by
        self._locator = locator

    def _find_element(self):
        """
        This methods validates the presence (but not visibility) of the element on the DOM within a DEFAULT_TIMEOUT
        period of 5 seconds. This method returns the web-element in successful case and logs an exception when
        failing to find the presence web-element.

        :return: web element
        """
        try:
            return WebDriverWait(self.driver, DefaultTimeouts.DEFAULT_TIMEOUT).until(ec.presence_of_element_located((self._by, self._locator)))
        except Exception as e:
            logger.exception("Timeout: Failed to find element {0}".format(self._locator))
            raise

    def find_sub_elements(self, by, locator):
        """
        TODO: return list of Element objects
        A wrapper around Selenium's find_elements()
        to return the sub element from a list of identified web elements.

        :param by: type of locator
        :param locator: uocator value
        :return: web element or an exception
        """
        return self._find_element().find_elements(by, locator)

    @property
    def driver(self):
        """
        This method calls Selenium's DriverFactory to build driver and returns the driver to be used in the tests
        :return: driver
        """
        return DriverRegistry.get_webdriver()

    @property
    def location(self):
        """
        This method identifies the web element and returns the location coordinates of the web element if the
        web element is found. Otherwise, logs an exception.
        :return: location coordinates
        """
        return self._find_element().location

    @property
    def size(self):
        """
        This method identifies the web element and returns the size (height and width) of the web element if the
        web element is found. Otherwise, logs an exception.
        :return: A dictionary with height and width
        """
        return self._find_element().size

    def exists(self):
        """
        This method can be used to validate the existence of the web element. Returns true if the web element exists and
        false with a debug log when the web element doesn't exists.
        :return: boolean
        """
        try:
            self._find_element()
            return True
        except Exception as e:
            logger.debug("Element {0} is not present in the DOM".format(self._locator))
            return False

    def _highlight(self):
        """
        If the highlight_state() is True and the element is visible, it synchronously executes the javascript to
        highlight the element that is visible.
        If the highlight_state() is False, no action is performed.
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
        :return: attributeValue
        """
        return self._find_element().get_attribute(attribute)

    def has_attribute(self, attribute):
        """
        This method helps to validate if the element and it's attribute value is present.
        Returns the attribute value if the element and it's attribute value is present and returns False otherwise.

        :param attribute: Name of the attribute/property to retrieve.
        :return: attributeValue or False
        """
        try:
            return self.get_attribute(attribute)
        except Exception:
            logger.debug("Element {0} does not have attribute {1}".format(self._locator, attribute))
            return False

    def get_css_property(self, css_property):
        """
        This method helps in retrieving the value of a CSS property.

        :param css_property: property name
        :return: property value
        """
        return self._find_element().value_of_css_property(css_property)

    def scroll_to_element(self, offset=200):
        """
         Synchronously Executes JavaScript to scroll to the element in the current window/frame.
        """
        self.driver.execute_script("window.scrollBy(0," + str(self.location['y'] - offset) + ");")

    # Visibility, Presence, Clickability

    def is_currently_visible(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        """
        This method will instantly (1 second) validate if the web element is is not only displayed but also has a
        height and width that is greater than 0. Returns the element if it is present. Returns False and
        logs a debug message if the element is not present.

        :param time: defaulted to LARGE_TIMEOUT of 10 second
        :return: element or False
         """
        return self.will_be_visible(time=time)

    def will_be_visible(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        """
        This method will wait for 10 seconds to validate if the web element is is not only displayed but also has a
        height and width that is greater than 0. Returns the element if it is present. Returns False and
        logs a debug message if the element is not present.

        :param time: defaulted to LARGE_TIMEOUT of 10 second
        :return: element or False
        """
        try:
            return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located((self._by, self._locator)))
        except Exception:
            logger.debug("Element {0} was not visible in time {1} secs".format(self._locator, str(time)))
            return False

    def is_currently_present(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        """
        This method will instantly (1 second) validate if the web element is present on the DOM of a page. This does
        not guarantee the visibility of the element though. Returns the element if it is present. Returns False and
        logs a debug message if the element is not present.

        :param time: defaulted to SHORT_TIMEOUT of 1 second
        :return: element or False
        """
        return self.will_be_present(time=time)

    def will_be_present(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        """
        This method will wait for 10 seconds to validate if the web element is present on the DOM of a page. This does
        not guarantee the visibility of the element though. Returns the element if it is present. Returns False and
        logs a debug message if the element is not present.

        :param time: defaulted to LARGE_TIMEOUT of 10 second
        :return: element or False
        """
        try:
            return WebDriverWait(self.driver, time).until(ec.presence_of_element_located((self._by, self._locator)))
        except Exception:
            logger.debug("Element {0} was not present in time {1} secs".format(self._locator, time))
            return False

    def is_not_displayed(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        """
        This method will instantly (1 second) look for a web element that is either invisible or not
        present on the DOM. Returns True if the element is invisible and False when visible.

        :param time: defaulted to SHORT_TIMEOUT of 1 second
        :return: boolean
        """
        return self.will_not_be_displayed(time=time)

    def will_not_be_displayed(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        """
        This method will wait for 10 seconds to validate if the web element is either invisible or not
        present on the DOM. Returns True if the element is invisible and False when visible.

        :param time: defaulted to LARGE_TIMEOUT of 10 second
        :return: boolean
        """
        try:
            return WebDriverWait(self.driver, time).until(ec.invisibility_of_element_located((self._by, self._locator)))
        except Exception:
            logger.debug("Element {0} was not invisible in time {1} secs".format(self._locator, time))
            return False

    def is_ready_to_interact(self, time=DefaultTimeouts.SHORT_TIMEOUT):
        """
        This method will instantly (1 second) look for a web element to enabled and be visible.

        If the element is enabled and visible within 1 seconds returns the web element for further action.
        If the web element is not enabled and visible within 10 seconds within 10 seconds, returns False and logs a
        debug message.

        :param time: defaulted to SHORT_TIMEOUT of 1 second
        :return: Web-element or False
        """
        return self.will_be_ready_to_interact(time=time)


    def will_be_ready_to_interact(self, time=DefaultTimeouts.LARGE_TIMEOUT):
        """
        This method will wait for a web element to enabled and be visible within 10 seconds.

        If the element is enabled and visible within 10 seconds, returns the web element for further action.
        If the web element is not enabled and visible within 10 seconds within 10 seconds, returns False and
        logs a debug message.

        :param time: defaulted to LARGE_TIMEOUT period of 10 seconds
        :return: Web-element or False
        """
        try:
            return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable((self._by, self._locator)))
        except Exception:
            logger.debug("Element {0} was not clickable in time {1} secs".format(self._locator, time))
            return False

    def hover_over(self):
        """
        This method helps in performing mouse hover over action using ActionChains, move_to_element and perform methods
        """
        hover = ActionChains(self.driver).move_to_element(self._find_element())
        hover.perform()

    def focus(self):
        """
        TODO: Implement focus function
        :return:
        """
        raise NotImplementedError
