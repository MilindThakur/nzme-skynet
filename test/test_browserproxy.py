# coding=utf-8
import unittest

from nzme_skynet.core.proxy.browserproxy import BrowserProxyLocal, BrowserProxyGrid
from nzme_skynet.core.driver.web.browserdriver import BrowserDriver
from browsermobproxy.client import Client


@unittest.skip("Need browsermob-proxy binary and driver for local test")
class BrowserProxyLocalTest(unittest.TestCase):

    TEST_URL = "https://www.google.co.nz/"
    BROWSER_PROXY_BIN = "/home/milindt/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy"

    def setUp(self):
        self.bproxy = BrowserProxyLocal(path_to_binary=self.BROWSER_PROXY_BIN)
        self.bproxy.start()

    def test_proxy_driver_instance(self):
        self.assertIsNotNone(self.bproxy.driver, BrowserDriver)
        self.assertIsNotNone(self.bproxy.client, Client)

    def test_recorded_har(self):
        self.bproxy.client.new_har(options={'captureHeaders': True})
        self.bproxy.driver.goto_url(self.TEST_URL, absolute=True)
        har = self.bproxy.client.har
        self.assertIsInstance(har, dict)

    def test_url_entry_matcher(self):
        har_page = self.bproxy.capture_url_traffic(url=self.TEST_URL)
        self.assertIsNotNone(har_page, "Error: Har is not created")
        match_list = self.bproxy.filter_entry_by_matching_url(har_page, "gstatic.com")
        self.assertGreater(len(match_list), 1)

    def tearDown(self):
        self.bproxy.stop()


class BrowserProxyGridTest(unittest.TestCase):

    TEST_URL = "https://www.google.co.nz/"

    def setUp(self):
        capabilities = {
            "browserName": "chrome",
            "platform": 'LINUX',
            "version": '',
            "javascriptEnabled": True
        }
        self.bproxy = BrowserProxyGrid(capabilities=capabilities)
        self.bproxy.start()

    def test_url_entry_matcher(self):
        har_page = self.bproxy.capture_url_traffic(url=self.TEST_URL)
        self.assertIsNotNone(har_page, "Error: Har is not created")
        match_list = self.bproxy.filter_entry_by_matching_url(har_page, "gstatic.com")
        self.assertGreater(len(match_list), 1)

    def tearDown(self):
        self.bproxy.stop()
