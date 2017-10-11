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
        with self.assertRaises(Exception) as context:
            DriverRegistry.get_driver()
        self.assertTrue("No registered driver found" in context.exception.message)

    def test_no_driver_deregistration_exception(self):
        with self.assertRaises(Exception) as context:
            DriverRegistry.deregister_driver()
        self.assertTrue('No registered driver found' in context.exception)

    # Chrome browser does not run in CI without headless mode.
    # Test should fail on CI but pass locally.
    @unittest.expectedFailure
    def test_default_chrome_local_driver_creation(self):
        DriverRegistry.register_driver()
        self.assertEqual(DriverRegistry.get_webdriver().name, DriverTypes.CHROME)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        DriverRegistry.deregister_driver()
        with self.assertRaises(Exception) as context:
            DriverRegistry.get_driver()
        self.assertTrue('No registered driver found' in context.exception)

    def test_custom_local_driver_registration(self):
        DriverRegistry.register_driver(DriverTypes.PHANTOMJS)
        self.assertEqual(DriverRegistry.get_webdriver().name, DriverTypes.PHANTOMJS)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        DriverRegistry.deregister_driver()
        with self.assertRaises(Exception) as context:
            DriverRegistry.get_driver()
        self.assertTrue('No registered driver found' in context.exception)

    def test_unsupported_local_driver_registration(self):
        with self.assertRaises(Exception) as context:
            DriverRegistry.register_driver(DriverTypes.IE)
        self.assertTrue('Only supports Chrome, Firefox, PhantomJS in local mode', context.exception.message)

    def test_default_remote_chrome_driver_registration(self):
        DriverRegistry.register_driver(local=False)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_webdriver().name, DriverTypes.CHROME)
        DriverRegistry.deregister_driver()
        with self.assertRaises(Exception) as context:
            DriverRegistry.get_driver()
        self.assertTrue('No registered driver found' in context.exception)

    def test_custom_remote_driver_registration(self):
        DriverRegistry.register_driver(driver_type=DriverTypes.FIREFOX, local=False)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_webdriver().name, DriverTypes.FIREFOX)
        DriverRegistry.deregister_driver()
        with self.assertRaises(Exception) as context:
            DriverRegistry.get_driver()
        self.assertTrue('No registered driver found' in context.exception)

    def test_unsupported_custom_remote_driver_registration(self):
        with self.assertRaises(Exception) as context:
            DriverRegistry.register_driver(driver_type=DriverTypes.IE, local=False)
        self.assertTrue('Only supports Chrome and Firefox in remote mode when no capabilities passed' in
                        context.exception.message)

    def test_remote_driver_registration_with_capabilities(self):
        test_capabilities = {
            "browserName": "chrome",
            "platform": 'LINUX',
            "version": '',
            "javascriptEnabled": True
        }
        DriverRegistry.register_driver(driver_options=test_capabilities, local=False)
        self.assertIsInstance(DriverRegistry.get_driver(), BrowserDriver)
        self.assertIsInstance(DriverRegistry.get_webdriver(), WebDriver)
        self.assertEqual(DriverRegistry.get_webdriver().name, DriverTypes.CHROME)
        DriverRegistry.deregister_driver()
        with self.assertRaises(Exception) as context:
            DriverRegistry.get_driver()
        self.assertTrue('No registered driver found' in context.exception)
