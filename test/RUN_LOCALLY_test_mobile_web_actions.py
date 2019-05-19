# coding=utf-8
import unittest
from selenium.webdriver.common.by import By

from nzme_skynet.core.controls.textinput import TextInput
from nzme_skynet.core.controls.button import Button
from nzme_skynet.core.controls.element import Element
from nzme_skynet.core.controls.text import Text
from nzme_skynet.core.driver.driverregistry import DriverRegistry
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes
from nzme_skynet.core.driver.mobile.browser.androidbrowserdriver import AndroidBrowserDriver

TEST_URL = "https://www.google.co.nz"
DOCKER_SELENIUM_URL = "http://localhost:4444/wd/hub"  # Appium server


class MobileWebActionsTestCase(unittest.TestCase):

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
            capabilities=cap,
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
        search_input = TextInput(By.NAME, 'q')
        search_btn = Button(
            By.CSS_SELECTOR, 'button[aria-label="Google Search"]')
        search_input.set_value("NZME")
        search_btn.click()
        results = Element(By.ID, 'ires')
        assert results.will_be_visible(), "Error: Results not visible"
        result_text = Text(By.CSS_SELECTOR, "#rso > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1)"
                                            " > a > div")
        assert result_text.has_text('NZME'), "Error: No NZME result found"

    @classmethod
    def tearDownClass(cls):
        DriverRegistry.deregister_driver()


if __name__ == "__main__":
    unittest.main()
