# coding=utf-8
import unittest

from nzme_skynet.core.browsers.localbrowserbuilder import LocalBrowserBuilder


class DriverInitTestCase(unittest.TestCase):
    def test_local_phantomjs_init(self):
        test_url = "http://www.bing.com/?cc=nz"
        lb = LocalBrowserBuilder("phantomJS", test_url)
        self.browser = lb.build()
        assert self.browser.get_base_url() == test_url
        assert self.browser.get_current_url() == test_url

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()