# coding=utf-8
from nzme_skynet.core.driver.mobile.app.mappdriver import MAppDriver
from appium.webdriver.webdriver import WebDriver
import logging
logger = logging.getLogger(__name__)


class AndroidAppDriver(MAppDriver):
    def __init__(self, desired_capabilities, remote_url):
        self._desired_cap = desired_capabilities
        self._driver = None
        self._remote_url = remote_url

    def init(self):
        self._create_driver()

    def _create_driver(self):
        logger.debug("Creating Android App driver")
        self._set_default_capabilities()
        self._driver = WebDriver(command_executor=self._remote_url, desired_capabilities=self._desired_cap)

    def _set_default_capabilities(self):
        self._create_desired_capabilities()

    def _create_desired_capabilities(self):
        if not self._desired_cap:
            raise Exception("No capabilities provided to init Appium driver")
        if 'platformVersion' not in self._desired_cap:
            raise Exception("Please provide platformVersion to test app against")
        if 'app' not in self._desired_cap:
            raise Exception("Please provide absolute app path for .apk")
        if 'appPackage' not in self._desired_cap:
            raise Exception("Please provide the java package of the app")
        if 'appActivity' not in self._desired_cap:
            raise Exception("Please provide the activity to launch")
        if 'deviceName' not in self._desired_cap:
            # Run tests on Android emulator by default
            self._desired_cap['deviceName'] = 'Android Emulator'
        self._desired_cap['platformName'] = 'Android'
        self._desired_cap['platform'] = 'ANDROID'

    @property
    def webdriver(self):
        # type: () -> WebDriver
        return self._driver
