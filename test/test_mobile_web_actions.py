# coding=utf-8
import unittest

from selenium.webdriver.common.by import By
from nzme_skynet.core.app import appbuilder
from nzme_skynet.core.browsers.web.browserTypes import BrowserTypes
from selenium.webdriver.chrome.options import Options


class MobileActionsTestCase(unittest.TestCase):
    TEST_URL = "https://www.google.co.nz"
    DOCKER_SELENIUM_URL = "http://localhost:4444/wd/hub"

    @classmethod
    def setUpClass(cls):
        cls.cap = {
                'selenium_grid_hub': 'http://localhost:4444/wd/hub',
                'platform': 'ANDROID',
                'platformName': 'Android',
                'deviceName': 'Android Emulator',
                'browserName': 'chrome',
                'version': '7.1.1',
                "chromeOptions": {"args": ["--no-first-run"]}
        }
        cls.app = appbuilder.build_mobile_browser(cls.cap, cls.TEST_URL)

    def test_driver_type(self):
        self.assertEqual(str(self.app.get_driver_type()), self.cap['platform'])
        self.assertEqual(self.app.appiumUrl, self.cap['appium_url'])

    def test_driver_can_get_session(self):
        assert self.app.get_driver().session_id is not None

    # def test_browser_setup(driver_setup):
    #     assert driver_setup.baseurl == TEST_URL
    #     assert (TEST_URL in driver_setup.get_current_url()) is True

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()


if __name__ == "__main__":
    unittest.main()
