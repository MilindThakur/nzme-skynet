# coding=utf-8
import unittest

from skynet.core.browsers.localbrowserbuilder import LocalBrowserBuilder


class DriverInitTestCase(unittest.TestCase):
    def test_local_phantomjs_init(self):
        test_url1 = "http://www.bing.com/?cc=nz"
        lb = LocalBrowserBuilder("phantomJS", test_url1)
        self.browser = lb.build()
        assert self.browser.get_base_url() == test_url1
        assert self.browser.get_current_url() == test_url1
        test_url2 = "https://www.google.co.nz/"
        self.browser.goto_absolute_url(test_url2)
        assert self.browser.get_base_url() == test_url2
        assert self.browser.get_current_url() == test_url2

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()