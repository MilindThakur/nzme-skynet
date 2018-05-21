# coding=utf-8
import time
import unittest

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver as AppiumDriver

from nzme_skynet.core.controls.melement import MElement
from nzme_skynet.core.driver.driverregistry import DriverRegistry
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes
from nzme_skynet.core.driver.mobile.app.androidappdriver import AndroidAppDriver

DOCKER_SELENIUM_URL = "http://localhost:4723/wd/hub"  # Appium server


class MobileActionsTestCase(unittest.TestCase):

    # app path for docker is /root/tmp/app-debug.apk
    # if running locally target ./test/mobile/testapps/app-debug.apk
    @classmethod
    def setUpClass(cls):
        cap = {
            'platformName': 'Android',
            'platformVersion': '7.1.1',
            'platform': 'Android',
            'deviceName': 'samsung_galaxy_s6_7.1.1',
            'app': '/root/tmp/app-debug.apk',
            "fullReset": "true",
            "appPackage": "nzme.test.skynettestapp",
            "appActivity": ".MainActivity"
        }

        cls.driver = DriverRegistry.register_driver(
            DriverTypes.ANDROID,
            driver_options=cap,
            grid_url=DOCKER_SELENIUM_URL)

    def test_driver_type(self):
        assert isinstance(self.driver, AndroidAppDriver)
        assert isinstance(self.driver.webdriver, AppiumDriver)
        self.assertIsNotNone(self.driver.webdriver.session_id)
        self.assertEqual(self.driver.context, 'NATIVE_APP')
        self.assertEqual(self.driver.webdriver.desired_capabilities['platform'], 'Android')
        self.assertIsNotNone(self.driver.webdriver.desired_capabilities['deviceUDID'])
        self.assertEqual(self.driver.current_activity, '.MainActivity')
        self.assertEqual(self.driver.webdriver.current_package, 'nzme.test.skynettestapp')

    def test_action_textinput(self):
        name_input = MElement(MobileBy.ID, "entertext_name_test")
        name_input.set_text("something")
        self.assertEqual(name_input.text, "something")

    def test_action_checkbox(self):
        agree_chk = MElement(MobileBy.ID, "checkBox_test")
        self.assertFalse(agree_chk.is_checked())
        agree_chk.click()
        self.assertTrue(agree_chk.is_checked())
        agree_chk.click()
        self.assertFalse(agree_chk.is_checked())

    @classmethod
    def tearDownClass(cls):
        DriverRegistry.deregister_driver()


if __name__ == "__main__":
    unittest.main()
