# coding=utf-8
from nzme_skynet.core.driver.mobile.app.mappdriver import MAppDriver


class AndroidAppDriver(MAppDriver):

    def __init__(self, desired_capabilities, remote_url='http://127.0.0.1:4444/wd/hub'):
        super(AndroidAppDriver, self).__init__(desired_capabilities, remote_url)

    def _create_desired_capabilities(self):
        if not self._desired_cap:
            raise Exception("No capabilities provided to init Appium driver")
        if not self._desired_cap['platformVersion']:
            raise Exception("Please provide platformVersion to test app against")
        if not self._desired_cap['app']:
            raise Exception("Please provide absolute app path for .apk")
        if not self._desired_cap['appPackage']:
            raise Exception("Please provide the java package of the app")
        if not self._desired_cap['appActivity']:
            raise Exception("Please provide the activity to launch")

        self._desired_cap['platformName'] = 'Android'
        self._desired_cap['platform'] = 'ANDROID'
        if not self._desired_cap['deviceName']:
            # Run tests on Android emulator by default
            self._desired_cap['deviceName'] = 'Android Emulator'


    def take_screenshot_current_window(self, filename):
        self.webdriver.get_screenshot_as_file(filename)
