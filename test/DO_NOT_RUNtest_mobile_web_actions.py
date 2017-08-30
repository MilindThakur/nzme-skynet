# coding=utf-8
import unittest
from nzme_skynet.core.app import appbuilder

TEST_URL = "https://www.google.co.nz"
DOCKER_SELENIUM_URL = "http://localhost:4444/wd/hub"


class MobileActionsTestCase(unittest.TestCase):

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
        cls.app = appbuilder.build_mobile_browser(cls.cap, TEST_URL)

    def test_driver_type(self):
        self.assertEqual(str(self.app.get_driver_type()), self.cap['platform'])
        self.assertEqual(self.app.selenium_grid_hub_url, self.cap['selenium_grid_hub'])

    def test_driver_can_get_session(self):
        assert self.app.driver.session_id is not None

    def test_browser_setup(setUpClass):
        assert (TEST_URL in setUpClass.app.get_current_url()) is True

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()


if __name__ == "__main__":
    unittest.main()
