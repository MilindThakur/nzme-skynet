# -*- coding: utf-8 -*-

import unittest

from nzme_skynet.core.driver.driverregistry import DriverRegistry
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.phantomjs.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes
from nzme_skynet.core.driver.web.browserdriver import BrowserDriver


class DriverFactoryTest(unittest.TestCase):

    def test_no_driver_registered_exception(self):
        self.assertIsNone(DriverRegistry.get_driver(),
                          'Error: Driver found without registration')

    def test_no_driver_deregistration_exception(self):
        self.assertIsNone(DriverRegistry.deregister_driver(),
                          'Error: Driver found without registration')

    # Chrome browser does not run in CI without headless mode.
    # Test should fail on CI but pass locally.
    @unittest.skip("Need Chrome binary and driver for local test")
    def test_default_chrome_local_driver_creation(self):
        DriverRegistry.register_driver()
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_driver().name, DriverTypes.CHROME)
        DriverRegistry.deregister_driver()
        self.assertIsNone(DriverRegistry.get_driver(),
                          'Error: Driver found without registration')

    # Chrome browser does not run in CI without headless mode.
    # Test should fail on CI but pass locally.
    @unittest.skip("Need FF binary and driver for local test")
    def test_ff_local_driver_registration(self):
        DriverRegistry.register_driver("firefox")
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_driver().name, DriverTypes.FIREFOX)
        DriverRegistry.deregister_driver()
        self.assertIsNone(DriverRegistry.get_driver(),
                          'Error: Driver found without registration')

    # Chrome browser does not run in CI without headless mode.
    # Test should fail on CI but pass locally.
    @unittest.skip("Need FF binary and driver for local test")
    def test_custom_local_driver_registration(self):
        test_capabilities = {
            "browserName": "firefox",
            "platform": 'LINUX',
            "version": '',
            "javascriptEnabled": True
        }
        DriverRegistry.register_driver(
            DriverTypes.FIREFOX, capabilities=test_capabilities)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_driver().name, DriverTypes.FIREFOX)
        DriverRegistry.deregister_driver()
        self.assertIsNone(DriverRegistry.get_driver(),
                          'Error: Driver found without registration')

    # Chrome browser does not run in CI without headless mode.
    # Test should fail on CI but pass locally.
    @unittest.skip("Need Chrome binary and driver for local test")
    def test_default_chrome_headless_local_driver_creation(self):
        option = {
            "highlight": True,
            "headless": True,
            "resolution": "maximum"
        }
        DriverRegistry.register_driver(options=option)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_driver().name, DriverTypes.CHROME)
        DriverRegistry.deregister_driver()
        self.assertIsNone(DriverRegistry.get_driver(),
                          'Error: Driver found without registration')

    # Chrome browser does not run in CI without headless mode.
    # Test should fail on CI but pass locally.
    @unittest.skip("Need FF binary and driver for local test")
    def test_ff_headless_local_driver_registration(self):
        option = {
            "highlight": True,
            "headless": True,
            "resolution": "maximum"
        }
        DriverRegistry.register_driver("firefox", options=option)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_driver().name, DriverTypes.FIREFOX)
        DriverRegistry.deregister_driver()
        self.assertIsNone(DriverRegistry.get_driver(),
                          'Error: Driver found without registration')

    def test_default_remote_chrome_driver_registration(self):
        DriverRegistry.register_driver(local=False)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_driver().name, DriverTypes.CHROME)
        DriverRegistry.deregister_driver()
        self.assertIsNone(DriverRegistry.get_driver(),
                          'Error: Driver found without registration')

    def test_remote_ff_driver_registration(self):
        DriverRegistry.register_driver(DriverTypes.FIREFOX, local=False)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_driver().name, DriverTypes.FIREFOX)
        DriverRegistry.deregister_driver()
        self.assertIsNone(DriverRegistry.get_driver(),
                          'Error: Driver found without registration')

    def test_remote_driver_registration_with_capabilities(self):
        test_capabilities = {
            "browserName": "firefox",
            "platform": 'LINUX',
            "version": '',
            "javascriptEnabled": True
        }
        DriverRegistry.register_driver(
            DriverTypes.FIREFOX, capabilities=test_capabilities, local=False)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_driver().name, DriverTypes.FIREFOX)
        DriverRegistry.deregister_driver()
        self.assertIsNone(DriverRegistry.get_driver(),
                          'Error: Driver found without registration')

    def test_remote_chrome_headless_driver_registration_with_capabilities(self):
        option = {
            "highlight": True,
            "headless": True,
            "resolution": "maximum"
        }
        DriverRegistry.register_driver(
            DriverTypes.CHROME, local=False, options=option)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_driver().name, DriverTypes.CHROME)
        DriverRegistry.deregister_driver()
        self.assertIsNone(DriverRegistry.get_driver(),
                          'Error: Driver found without registration')

    def test_remote_ff_headless_driver_registration_with_capabilities(self):
        option = {
            "highlight": True,
            "headless": True,
            "resolution": "maximum"
        }
        DriverRegistry.register_driver(
            DriverTypes.FIREFOX, local=False, options=option)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_driver().name, DriverTypes.FIREFOX)
        DriverRegistry.deregister_driver()
        self.assertIsNone(DriverRegistry.get_driver(),
                          'Error: Driver found without registration')

    def test_remote_chrome_with_capabilities_and_with_options(self):
        capabilities = {
            "browserName": "chrome",
            "version": "ANY",
            "platform": "ANY"
        }

        option = {
            "highlight": True,
            "headless": True,
            "resolution": "maximum",
            "mobileEmulation": "iPhone X"
        }
        DriverRegistry.register_driver(local=False, capabilities=capabilities, options=option)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_driver().name, DriverTypes.CHROME)
        DriverRegistry.deregister_driver()
        self.assertIsNone(DriverRegistry.get_driver(),
                          'Error: Driver found without registration')

    def test_remote_chrome_with_custom_capabilities_chomeoptions_and_with_options(self):
        capabilities = {
            "browserName": "chrome",
            "version": "ANY",
            "platform": "ANY",
            "goog:chromeOptions": {
                "args": ["--disable-gpu", "--no-sandbox"],
                "extensions": [],
                "prefs": {}
            }
        }

        option = {
            "highlight": True,
            "headless": True,
            "resolution": "maximum",
            "mobileEmulation": "iPhone X"
        }
        DriverRegistry.register_driver(local=False, capabilities=capabilities, options=option)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_driver().name, DriverTypes.CHROME)
        DriverRegistry.deregister_driver()
        self.assertIsNone(DriverRegistry.get_driver(),
                          'Error: Driver found without registration')

    def test_registering_multiple_drivers(self):
        DriverRegistry.register_driver(DriverTypes.CHROME, local=False)
        current_driver = DriverRegistry.get_driver()
        new_driver = DriverRegistry.register_driver(DriverTypes.FIREFOX)
        self.assertIsNotNone(
            new_driver, "Error: Should return previously registered driver")
        self.assertEqual(current_driver, new_driver,
                         "Error: Should return same driver instance created before")
        DriverRegistry.deregister_driver()
        self.assertIsNone(DriverRegistry.get_driver(),
                          'Error: Driver found without registration')
        self.assertIsNone(DriverRegistry.get_webdriver(),
                          'Error: Webdriver found without registration')

    def test_unsupported_local_driver_registration(self):
        with self.assertRaises(Exception) as context:
            DriverRegistry.register_driver(driver_type="random")
        self.assertTrue(
            'Empty or Unknown driver type, valid options: chrome, firefox, safari, ie android, ios', context.exception)
