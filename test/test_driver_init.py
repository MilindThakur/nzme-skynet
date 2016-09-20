# coding=utf-8
import unittest

from nzme_skynet.core.app import appbuilder
from nzme_skynet.core.browsers.web.browserTypes import BrowserTypes


class DriverInitTestCase(unittest.TestCase):

    TEST_URL = "http://127.0.0.1:8000/"

    @classmethod
    def setUpClass(cls):
        cls.app = appbuilder.build_desktop_browser("chrome")
        cls.app.goto_url(cls.TEST_URL)

    def test_browser_type(self):
        self.assertEqual(self.app.get_browser_type(), BrowserTypes.CHROME)
        self.assertEqual(self.app.base_url, self.TEST_URL)

    def test_action_input(self):
        input = self.app.get_actions().textinput("css_selector")
        image = self.app.get_actions().image("locator")
        self.assertEqual(input.get_value(), "Sample Text")
        input.set_value("something")
        self.assertEqual(input.get_value(), "something")

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()