# coding=utf-8
import unittest

from nzme_skynet.core.proxy.har import Har


class HarTestCase(unittest.TestCase):

    TEST_URL = "https://www.google.co.nz/"

    def setUp(self):
        self.har = Har()
        self.har.start()

    def test_har_creation(self):
        har_page = self.har.create_har_page(self.TEST_URL, "google")
        self.assertIsNotNone(har_page, "Error: Har is not created")
        self.assertEqual(har_page.url, self.TEST_URL, "Error: Does not match Har request url {0}".format(self.TEST_URL))
        entries = har_page.filter_entries(content_type='image.*', status_code='2.*')
        self.assertEqual(len(entries), 3, "Error: Expected 3 entries do not match found {0} entries"
                         .format(len(entries)))

    def test_url_entry_matcher(self):
        har_page = self.har.create_har_page(self.TEST_URL, "google_url_matcher")
        self.assertIsNotNone(har_page, "Error: Har is not created")
        match_list = self.har.filter_entry_by_matching_url(har_page, "gstatic.com")
        self.assertEqual(len(match_list), 2)

    def tearDown(self):
        self.har.stop()
