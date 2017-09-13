# coding=utf-8
import unittest

from nzme_skynet.core.proxy.har import Har


class HarTestCase(unittest.TestCase):

    TEST_URL = "https://www.google.co.nz/"

    def setUp(self):
        self.har = Har(local_run=False)
        self.har.start()

    def test_url_entry_matcher(self):
        har_page = self.har.create_har_page(self.TEST_URL, "google_url_matcher")
        self.assertIsNotNone(har_page, "Error: Har is not created")
        match_list = self.har.filter_entry_by_matching_url(har_page, "gstatic.com")
        self.assertEqual(len(match_list), 2)

    def tearDown(self):
        self.har.stop()
