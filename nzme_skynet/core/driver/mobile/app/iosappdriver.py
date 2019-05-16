# coding=utf-8
from nzme_skynet.core.controls.enums.timeouts import DefaultTimeouts
from nzme_skynet.core.driver.mobile.app.mappdriver import MAppDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
logger = logging.getLogger(__name__)


class IOSAppDriver(MAppDriver):

    def _create_desired_capabilities(self):
        if not self._desired_cap:
            raise Exception("No capabilities provided to init Appium driver")
        if 'platformVersion' not in self._desired_cap:
            raise Exception(
                "Please provide platformVersion to test app against")
        if 'bundleId' not in self._desired_cap:
            raise Exception("Please provide bundle ID")
        if 'app' not in self._desired_cap:
            raise Exception(
                "Please provide absolute app path for .app or .ipa")
        if 'deviceName' not in self._desired_cap:
            # Run tests on simulator by default
            self._desired_cap['deviceName'] = 'iPhone X'
        if 'automation' not in self._desired_cap:
            self._desired_cap['automation'] = 'XCUITest'
        if 'fullReset' not in self._desired_cap:
            self._desired_cap['fullReset'] = 'true'
        if 'platformName' not in self._desired_cap:
            self._desired_cap['platformName'] = 'iOS'
        logger.debug(
            "Received iOS capability for creating driver {0}".format(self._desired_cap))

    def accept_location_popup(self, secondstowait=DefaultTimeouts.DEFAULT_TIMEOUT):
        logger.debug("Attempting to accept Location Popup..")
        try:
            alert = WebDriverWait(self._driver, secondstowait).until(EC.alert_is_present(),
                                                                     'Timed out waiting for Location Services ' +
                                                                     'confirmation popup to appear.')
            alert.accept()
        except Exception as e:
            logger.debug("Failed to accept alert: {}".format(e.message))
            raise
