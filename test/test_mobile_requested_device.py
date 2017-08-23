# coding=utf-8
import unittest

from selenium.webdriver.common.by import By
from nzme_skynet.core.app import appbuilder
from nzme_skynet.core.browsers.web.browserTypes import BrowserTypes


class MobileActionsTestCase(unittest.TestCase):
    TEST_URL = "http://localhost:4444/"

    # app path for docker is /root/tmp/app-debug.apk
    # if running locally target ./test/mobile/testapps/app-debug.apk
    def test_generic_device_caps(self):
        cap = {"deviceName": "Android Emulator",
               "appium_url": "http://localhost:4444/wd/hub",
               "platform": "android",
               "platformName": "Android",
               "app": "/root/tmp/app-debug.apk",
               "fullReset": "true",
               "appPackage": "nzme.test.skynettestapp",
               "appActivity": ".MainActivity"}
        self.app = appbuilder.build_appium_driver(cap)
        assert self.app.get_driver().session_id is not None
        self.app.quit()

    #specific to docker setup.
    def test_specific_device_caps(self):
        cap = {"deviceName": "Android Emulator",
               "appium_url": "http://localhost:4444/wd/hub",
               "platform": "android",
               "platformName": "Android",
               "version": "6.0",
               "app": "/root/tmp/app-debug.apk",
               "fullReset": "true",
               "appPackage": "nzme.test.skynettestapp",
               "appActivity": ".MainActivity"}
        self.app = appbuilder.build_appium_driver(cap)
        assert self.app.get_driver().session_id is not None
        self.app.quit()

    @classmethod
    def tearDownClass(cls):
        try:
            cls.app.quit()
        except Exception:
            raise

if __name__ == "__main__":
    unittest.main()
