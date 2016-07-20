# coding=utf-8
import unittest

from core.browser.localbrowserbuilder import LocalBrowserBuilder


class test_driver_init(unittest.TestCase):
    def test_local_chrome_init(self):
        lb = LocalBrowserBuilder("chrome", "https://www.google.co.nz")
        self.browser = lb.build()
        assert self.browser.get_base_url() == "https://www.google.co.nz"
        assert self.browser.get_current_url() == "https://www.google.co.nz/"
        self.browser.goto_url("http://www.bing.com/?cc=nz")
        assert self.browser.get_current_url() == "http://www.bing.com/?cc=nz"

    def tearDown(self):
        self.browser.quit_webdriver()
