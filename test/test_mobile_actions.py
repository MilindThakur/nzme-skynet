# coding=utf-8
import unittest
from nzme_skynet.core.app import appbuilder


class MobileActionsTestCase(unittest.TestCase):

    # app path for docker is /root/tmp/app-debug.apk
    # if running locally target ./test/mobile/testapps/app-debug.apk
    @classmethod
    def setUpClass(cls):
        cls.cap = {"deviceName": "Android Emulator",
               "appium_url": "http://localhost:4444/wd/hub",
               "platform": "android",
               "platformName": "Android",
               "app": "/root/tmp/app-debug.apk",
               #"app": "/home/stefankahn/PycharmProjects/skynet/test/mobile/testapps/app-debug.apk",
               "fullReset": "true",
               "appPackage": "nzme.test.skynettestapp",
               "appActivity": ".MainActivity"}
        cls.app = appbuilder.build_appium_driver(cls.cap)

    def test_driver_type(self):
        self.assertEqual(str(self.app.get_driver_type()), self.cap['platform'])
        self.assertEqual(self.app.appiumUrl, self.cap['appium_url'])

    def test_driver_can_get_session(self):
        assert self.app.get_driver().session_id is not None

    def test_can_install_app(self):
        self.assertTrue(self.app.is_app_installed())

    def can_get_element(self):
        self.assertNotEquals(None, self.app.get_actions().mobelement("navigation_dashboard"))

    def test_can_tap_on_element(self):
        initial_page_source = self.app.get_page_source()
        self.app.get_actions().mobelement("navigation_dashboard").click()
        self.assertNotEquals(initial_page_source, self.app.get_page_source(), "Page source did not change after "
                                                                              "element was clicked")

    def test_can_get_attributes(self):
        checkbox = self.app.get_actions().mobelement("checkBox_test")
        self.assertEqual("false", checkbox.get_attr("checked"))

    def test_action_textinput(self):
        txt_input = self.app.get_actions().mobelement("entertext_name_test")
        txt_input.set_text("")
        self.assertEqual(txt_input.get_text(), "")
        txt_input.set_value("something")
        self.assertEqual(txt_input.get_text(), "something")

    def test_action_button(self):
        submit_btn = self.app.get_actions().mobelement("toggleButton_test")
        self.assertEqual(submit_btn.get_text(), "OFF")

    def test_action_checkbox(self):
        agree_chk = self.app.get_actions().mobelement("checkBox_test")
        self.assertFalse(agree_chk.is_checked())
        agree_chk.click()
        self.assertTrue(agree_chk.is_checked())
        agree_chk.click()
        self.assertFalse(agree_chk.is_checked())

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()


if __name__ == "__main__":
    unittest.main()
