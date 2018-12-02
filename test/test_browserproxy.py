# coding=utf-8
import unittest

from nzme_skynet.core.proxy.browserproxy import BrowserProxy


class HarTestCase(unittest.TestCase):

    TEST_URL = "https://www.google.co.nz/"

    def setUp(self):
        self.proxy = BrowserProxy(local_run=False)
        self.proxy.start()

    def test_url_entry_matcher(self):
        har_page = self.proxy.create_har_page(self.TEST_URL, "google_url_matcher")
        self.assertIsNotNone(har_page, "Error: Har is not created")
        match_list = self.proxy.filter_entry_by_matching_url(har_page, "gstatic.com")
        self.assertGreater(len(match_list), 1)

    def tearDown(self):
        self.proxy.stop()
