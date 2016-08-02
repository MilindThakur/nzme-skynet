# coding=utf-8
import unittest

from core.browser.localbrowserbuilder import LocalBrowserBuilder


class DriverInitTestCase(unittest.TestCase):
    def test_local_chrome_init(self):
        lb = LocalBrowserBuilder("phantomJS", "https://www.google.co.nz")
        self.browser = lb.build()
        assert self.browser.get_base_url() == "https://www.google.co.nz"
        assert self.browser.get_current_url() == "https://www.google.co.nz/"
        self.browser.goto_absolute_url("http://www.bing.com/?cc=nz")
        assert self.browser.get_base_url() == "http://www.bing.com/?cc=nz"
        assert self.browser.get_current_url() == "http://www.bing.com/?cc=nz"

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()