# -*- coding: utf-8 -*-
from nzme_skynet.core.driver.mobile.mobiledriver import MobileDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from nzme_skynet.core.controls.enums.timeouts import DefaultTimeouts
import logging
logger = logging.getLogger(__name__)


class MAppDriver(MobileDriver):

    def __init__(self, desired_capabilities, remote_url='http://127.0.0.1:4444/wd/hub'):
        super(MAppDriver, self).__init__(desired_capabilities, remote_url)
        # Cache the App context view for switching between WEBVIEW and NATIVE_APP view
        self._cache_context = None

    def close_app(self):
        logger.debug("Closing app..")
        self.webdriver.close_app()

    def reset(self):
        logger.debug("Resetting the app..")
        self.webdriver.reset()

    # TODO: Assume the mobile app tests always start in NATIVE_APP context
    # and the second context is always WEBVIEW_. This login may require change
    # if the context array is > 2
    def switch_to_webview(self):
        if 'NATIVE_APP' in self.context:
            logger.debug("App running in NATIVE VIEW")
            self._cache_context = self.webdriver.context
        try:
            WebDriverWait(self.webdriver, DefaultTimeouts.DEFAULT_TIMEOUT).\
                until(lambda driver: len(driver.contexts) > 1)
            self.webdriver.switch_to.context(self.webdriver.contexts[1])
        except TimeoutException:
            raise TimeoutException(
                "Page elements never fully loaded after %s seconds" % DefaultTimeouts.DEFAULT_TIMEOUT)
        # self.webdriver.switch_to.context(self.webdriver.contexts[1])

    # TODO: Assuming the contexts are always available. In case its not,
    # revert to the cached context
    def switch_to_native(self):
        try:
            if 'WEBVIEW' in self.context:
                logger.debug("App in WEBVIEW, switching to NATIVE VIEW..")
                self.webdriver.switch_to.context(self.webdriver.contexts[0])
        except:
            self.webdriver.switch_to.context(self._cache_context)

    @property
    def current_activity(self):
        return self.webdriver.current_activity
