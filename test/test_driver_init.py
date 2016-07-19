# coding=utf-8
import unittest

from core.browser.localbrowserbuilder import LocalBrowserBuilder


class test_driver_init(unittest.TestCase):

    def setUp(self):
        self.webdriver_path = "/home/milindt/Downloads/chromedriver"

    def test_local_chrome_init_default(self):
        lb = LocalBrowserBuilder("chrome", "https://www.google.com")
        self.br = lb.build()
        assert self.br.get_base_url() == "https://www.google.com"
        self.br.set_base_url("http://www.nzherald.co.nz")
        assert self.br.get_base_url() == "http://www.nzherald.co.nz"

    def test_local_chrome_init_webdriverpath(self):
        lb = LocalBrowserBuilder("chrome", "https://www.google.com", webDriverPath=self.webdriver_path)
        self.br = lb.build()
        assert self.br.get_base_url() == "https://www.google.com"

    def tearDown(self):
        self.br.quit_webdriver()
