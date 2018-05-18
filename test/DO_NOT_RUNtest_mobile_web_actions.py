# coding=utf-8
import unittest

from nzme_skynet.core.driver.driverregistry import DriverRegistry
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes
from nzme_skynet.core.driver.mobile.browser.androidbrowserdriver import AndroidBrowserDriver

TEST_URL = "https://www.google.co.nz"
DOCKER_SELENIUM_URL = "http://localhost:4444/wd/hub"


class MobileActionsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cap = {
            'platformName': 'Android',
            'version': '7.1.1',
            'platform': 'Android',
            'deviceName': 'samsung_galaxy_s6_7.1.1',
            'browserName': 'chrome'
        }
        cls.driver = DriverRegistry.register_driver(
            DriverTypes.ANDROIDWEB,
            driver_options=cap,
            grid_url=DOCKER_SELENIUM_URL)

    def test_driver_type(self):
        assert isinstance(self.driver, AndroidBrowserDriver)
        assert self.driver.name == 'chrome'
        assert self.driver.context == 'CHROMIUM'
        assert self.driver.webdriver.desired_capabilities['version'] == '7.1.1'
        assert self.driver.webdriver.desired_capabilities['browserName'] == 'chrome'
        assert self.driver.webdriver.session_id is not None

    def test_browser_setup(self):
        self.driver.goto_url(TEST_URL, absolute=True)
        assert TEST_URL in self.driver.current_url
        assert 'Google' in self.driver.title

    @classmethod
    def tearDownClass(cls):
        DriverRegistry.deregister_driver()


if __name__ == "__main__":
    unittest.main()
