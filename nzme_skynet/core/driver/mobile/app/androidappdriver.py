# coding=utf-8
from nzme_skynet.core.driver.mobile.app.mappdriver import MAppDriver
import logging
logger = logging.getLogger(__name__)


class AndroidAppDriver(MAppDriver):

    def _create_desired_capabilities(self):
        if not self._desired_cap:
            raise Exception("No capabilities provided to init Appium driver")
        if 'platformVersion' not in self._desired_cap:
            raise Exception(
                "Please provide platformVersion to test app against")
        if 'app' not in self._desired_cap:
            raise Exception("Please provide absolute app path for .apk")
        if 'appPackage' not in self._desired_cap:
            raise Exception("Please provide the java package of the app")
        if 'appActivity' not in self._desired_cap:
            raise Exception("Please provide the activity to launch")
        if 'deviceName' not in self._desired_cap:
            # Run tests on Android emulator by default
            self._desired_cap['deviceName'] = 'Android Emulator'
        if 'fullReset' not in self._desired_cap:
            self._desired_cap['fullReset'] = 'true'
        self._desired_cap['platformName'] = 'Android'
        logger.debug("Received Android capability for creating driver: {0}".format(
            self._desired_cap))
