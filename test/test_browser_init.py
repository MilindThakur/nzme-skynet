import unittest
from nzme_skynet.core.driver.web.browsers.chrome import Chrome
from nzme_skynet.core.driver.web.browsers.firefox import Firefox
from nzme_skynet.core.driver.web.browsers.safari import Safari


class TestBrowserDriverInit(unittest.TestCase):

    def test_chrome_init_without_cap_options(self):
        chrome = Chrome(capabilities=None, options=None)
        self.assertIsNone(chrome._capabilities)
        self.assertIsNone(chrome._options)
        chrome._update_capabilities_with_options()
        self.assertIsNotNone(chrome._capabilities)
        self.assertEqual(len(chrome._capabilities), 4)
        self.assertTrue("browserName" in chrome._capabilities)
        self.assertEqual(chrome._capabilities["browserName"], "chrome")
        self.assertTrue("version" in chrome._capabilities)
        self.assertEqual(chrome._capabilities['version'], '')
        self.assertTrue("platform" in chrome._capabilities)
        self.assertEqual(chrome._capabilities['platform'], 'ANY')
        self.assertTrue("goog:chromeOptions" in chrome._capabilities)
        self.assertTrue('args' in chrome._capabilities['goog:chromeOptions'])
        self.assertEqual(len(chrome._capabilities['goog:chromeOptions']['args']), 4)
        self.assertIsNone(chrome._options, None)

    def test_chrome_init_with_cap_only(self):
        cap = {
            "browserName": "chrome",
            "version": "ANY",
            "platform": "ANY"
        }
        chrome = Chrome(capabilities=cap, options=None)
        self.assertIsNone(chrome._options)
        self.assertIsNotNone(chrome._capabilities)
        chrome._update_capabilities_with_options()
        self.assertTrue("browserName" in chrome._capabilities)
        self.assertEqual(chrome._capabilities["browserName"], "chrome")
        self.assertTrue("version" in chrome._capabilities)
        self.assertEqual(chrome._capabilities['version'], 'ANY')
        self.assertTrue("platform" in chrome._capabilities)
        self.assertEqual(chrome._capabilities['platform'], 'ANY')
        self.assertTrue("goog:chromeOptions" in chrome._capabilities)
        self.assertIsNone(chrome._options)

    def test_chrome_init_with_options_only(self):
        opt = {
            "headless": True,
            "resolution": "maximum",
            "mobileEmulation": "iPhone X"
        }
        chrome = Chrome(capabilities=None, options=opt)
        self.assertIsNone(chrome._capabilities)
        self.assertEqual(chrome._options, opt)
        chrome._update_capabilities_with_options()
        self.assertIsNotNone(chrome._capabilities)
        self.assertEqual(chrome._capabilities["browserName"], "chrome")
        self.assertTrue("version" in chrome._capabilities)
        self.assertEqual(chrome._capabilities['version'], '')
        self.assertTrue("platform" in chrome._capabilities)
        self.assertEqual(chrome._capabilities['platform'], 'ANY')
        self.assertTrue("goog:chromeOptions" in chrome._capabilities)
        self.assertEqual(len(chrome._capabilities['goog:chromeOptions']['args']), 7)
        self.assertTrue(
            "--headless" in chrome._capabilities["goog:chromeOptions"]["args"])
        self.assertTrue(
            "mobileEmulation" in chrome._capabilities["goog:chromeOptions"])

    def test_chrome_init_with_cap_and_options(self):
        cap = {
            "browserName": "chrome",
            "version": "ANY",
            "platform": "ANY"
        }
        opt = {
            "headless": True,
            "resolution": "maximum",
            "mobileEmulation": "iPhone X"
        }
        chrome = Chrome(capabilities=cap, options=opt)
        self.assertEqual(chrome._capabilities, cap)
        self.assertEqual(chrome._options, opt)
        chrome._update_capabilities_with_options()
        self.assertEqual(chrome._capabilities["browserName"], "chrome")
        self.assertTrue("version" in chrome._capabilities)
        self.assertEqual(chrome._capabilities['version'], 'ANY')
        self.assertTrue("platform" in chrome._capabilities)
        self.assertEqual(chrome._capabilities['platform'], 'ANY')
        self.assertTrue("goog:chromeOptions" in chrome._capabilities)
        self.assertEqual(len(chrome._capabilities['goog:chromeOptions']['args']), 7)
        self.assertTrue(
            "--headless" in chrome._capabilities["goog:chromeOptions"]["args"])
        self.assertTrue(
            "mobileEmulation" in chrome._capabilities["goog:chromeOptions"])

    def test_chrome_with_options_in_cap(self):
        cap = {
            "browserName": "chrome",
            "version": "ANY",
            "platform": "ANY",
            "goog:chromeOptions": {
                "args": ["--some-args"]
            }
        }
        opt = {
            "headless": False,
            "resolution": "maximum",
            "mobileEmulation": ""
        }
        chrome = Chrome(capabilities=cap, options=opt)
        self.assertEqual(chrome._capabilities, cap)
        self.assertEqual(chrome._options, opt)
        chrome._update_capabilities_with_options()
        self.assertEqual(chrome._capabilities["browserName"], "chrome")
        self.assertTrue("version" in chrome._capabilities)
        self.assertEqual(chrome._capabilities['version'], 'ANY')
        self.assertTrue("platform" in chrome._capabilities)
        self.assertEqual(chrome._capabilities['platform'], 'ANY')
        self.assertTrue("goog:chromeOptions" in chrome._capabilities)
        self.assertEqual(len(chrome._capabilities['goog:chromeOptions']['args']), 5)
        self.assertFalse(
            "--headless" in chrome._capabilities["goog:chromeOptions"]["args"], chrome._capabilities)
        self.assertTrue(
            "--some-args" in chrome._capabilities["goog:chromeOptions"]["args"])
        self.assertFalse(
            "mobileEmulation" in chrome._capabilities["goog:chromeOptions"])

    def test_ff_init_with_cap_and_options(self):
        cap = {
            "browserName": "firefox",
            "version": "ANY",
            "platform": "ANY"
        }
        opt = {
            "headless": True,
            "resolution": "maximum",
            "mobileEmulation": ""
        }
        ff = Firefox(capabilities=cap, options=opt)
        self.assertEqual(ff._capabilities, cap)
        self.assertEqual(ff._options, opt)
        ff._update_capabilities_with_options()
        self.assertTrue("moz:firefoxOptions" in ff._capabilities)
        self.assertTrue(
            "-headless" in ff._capabilities["moz:firefoxOptions"]["args"])
        self.assertFalse(
            "mobileEmulation" in ff._capabilities["moz:firefoxOptions"])

    def test_ff_init_with_cap_custom_mozffoptions_and_options(self):
        cap = {
            "browserName": "firefox",
            "version": "ANY",
            "platform": "ANY",
            "moz:firefoxOptions": {
                "args": ["-some-args"],
                "binary": "/usr/local/firefox/bin/firefox",
                "prefs": {
                    "dom.ipc.processCount": 8,
                    "javascript.options.showInConsole": False
                },
                "log": {"level": "trace"}
            }
        }
        opt = {
            "headless": True,
            "resolution": "maximum",
            "mobileEmulation": ""
        }
        ff = Firefox(capabilities=cap, options=opt)
        self.assertEqual(ff._capabilities, cap)
        self.assertEqual(ff._options, opt)
        ff._update_capabilities_with_options()
        self.assertTrue("moz:firefoxOptions" in ff._capabilities)
        self.assertTrue(
            "-headless" in ff._capabilities["moz:firefoxOptions"]["args"])
        self.assertTrue(
            "-some-args" in ff._capabilities["moz:firefoxOptions"]["args"])
        self.assertEqual(len(ff._capabilities["moz:firefoxOptions"]), 4)
        self.assertTrue("binary" in ff._capabilities["moz:firefoxOptions"])
        self.assertTrue("prefs" in ff._capabilities["moz:firefoxOptions"])
        self.assertTrue("log" in ff._capabilities["moz:firefoxOptions"])
        self.assertFalse(
            "mobileEmulation" in ff._capabilities["moz:firefoxOptions"])

    def test_safari_init_with_cap_and_options(self):
        cap = {
            "browserName": "safari",
            "version": "ANY",
            "platform": "ANY"
        }
        opt = {
            "headless": True,
            "resolution": "maximum",
            "mobileEmulation": ""
        }
        safari = Safari(capabilities=cap, options=opt)
        self.assertEqual(safari._capabilities, cap)
        self.assertEqual(safari._options, opt)
        safari._update_capabilities_with_options()
        self.assertEqual(len(safari._capabilities), 3)
        self.assertEqual(safari._capabilities, cap)

    def test_browserstack_capability_init(self):
        cap = {
            'os': 'Windows',
            'os_version': '10',
            'browser': 'Chrome',
            'browser_version': '73.0',
            'resolution': '1920x1080',
            'project': 'test_proj',
            'build': 'test_build',
            'name': 'test_name',
            'browserstack.local': 'true',
            'browserstack.debug': 'true',
            'browserstack.selenium_version': '3.14.0'
        }
        opt = {
            "headless": True,
            "resolution": "maximum",
            "mobileEmulation": ""
        }
        chrome = Chrome(capabilities=cap, options=opt)
        self.assertEqual(chrome._capabilities, cap)
        self.assertEqual(chrome._options, opt)
        chrome._update_capabilities_with_options()
        self.assertTrue("goog:chromeOptions" in chrome._capabilities)
        self.assertTrue(
            "--headless" in chrome._capabilities["goog:chromeOptions"]["args"])
        self.assertFalse(
            "mobileEmulation" in chrome._capabilities["goog:chromeOptions"])
        self.assertEqual(len(chrome._capabilities), 12)
