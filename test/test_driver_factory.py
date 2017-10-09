# -*- coding: utf-8 -*-

import unittest

from nzme_skynet.core.driver.driverfactory import DriverFactory
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.phantomjs.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver


class DriverFactoryTest(unittest.TestCase):

    # Chrome browser does not run in CI without headless mode.
    # Test should fail on CI but pass locally.
    @unittest.expectedFailure
    def test_default_chrome_local_driver_creation(self):
        def_driver = DriverFactory()
        with self.assertRaises(Exception) as context:
            def_driver.get_driver_by_name('chrome')
        self.assertTrue('No driver has registered' in context.exception)
        test_driver = def_driver.register_driver()
        self.assertEqual('chrome', test_driver.name)
        self.assertIsInstance(test_driver, WebDriver)
        def_driver.deregister_driver()
        with self.assertRaises(Exception) as context:
            def_driver.get_driver_by_name('chrome')
        self.assertTrue('No driver has registered' in context.exception)

    def test_custom_local_driver_registration(self):
        def_driver = DriverFactory()
        test_driver = def_driver.register_driver('phantomjs')
        self.assertIsInstance(test_driver, WebDriver)
        self.assertEqual('phantomjs', test_driver.name)
        def_driver.deregister_driver()
        with self.assertRaises(Exception) as context:
            def_driver.get_driver_by_name('phantomjs')
        self.assertTrue('No driver has registered' in context.exception)

    def test_default_remote_chrome_driver_registration(self):
        def_driver = DriverFactory()
        def_driver.set_run_env(local=False)
        test_remote_driver = def_driver.register_driver()
        self.assertIsInstance(test_remote_driver, WebDriver)
        self.assertEqual('chrome', test_remote_driver.name)
        def_driver.deregister_driver()

    def test_custom_remote_driver_registration(self):
        def_driver = DriverFactory()
        def_driver.set_run_env(local=False)
        test_remote_driver = def_driver.register_driver('firefox')
        self.assertIsInstance(test_remote_driver, WebDriver)
        self.assertEqual('firefox', test_remote_driver.name)
        def_driver.deregister_driver()

    def test_unsupported_custom_remote_driver_registration(self):
        def_driver = DriverFactory()
        def_driver.set_run_env(local=False)
        with self.assertRaises(Exception) as context:
            def_driver.register_driver('phantomjs')
        self.assertTrue('Only supports Chrome and Firefox in remote mode when no capabilities passed' in
                        context.exception.message)

    def test_remote_driver_registration_with_capabilities(self):
        def_driver = DriverFactory()
        def_driver.set_run_env(local=False)
        test_capabilities = {
            "browserName": "chrome",
            "platform": 'LINUX',
            "version": '',
            "javascriptEnabled": True
        }
        test_remote_driver = def_driver.register_driver(capabilities=test_capabilities)
        self.assertIsInstance(test_remote_driver, WebDriver)
        self.assertEqual('chrome', test_remote_driver.name)
        def_driver.deregister_driver()
