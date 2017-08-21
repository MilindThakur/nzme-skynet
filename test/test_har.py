# coding=utf-8
import unittest

from nzme_skynet.core.proxy.har import Har


class HarTestCase(unittest.TestCase):

    TEST_URL = "https://www.google.co.nz/"

    def setUp(self):
        self.har = Har()
        self.har.start()

    def testHarCreation(self):
        har_page = self.har.create_har_page(self.TEST_URL, "google")
        self.assertIsNotNone(har_page, "Error: Har is not created")
        self.assertEqual(har_page.url, self.TEST_URL, "Error: Does not match Har request url {0}".format(self.TEST_URL))
        entries = har_page.filter_entries(content_type='image.*', status_code='2.*')
        self.assertEqual(len(entries), 3, "Error: Expected 3 entries do not match found {0} entries"
                         .format(len(entries)))

    def tearDown(self):
        self.har.stop()
