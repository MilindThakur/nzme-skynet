# coding=utf-8
import unittest

from selenium.webdriver.common.by import By

from nzme_skynet.core.actions.enums.checkboxstates import CheckboxState
from nzme_skynet.core.app import appbuilder
from nzme_skynet.core.browsers.web.browserTypes import BrowserTypes


class ActionsTestCase(unittest.TestCase):
    TEST_URL = "http://127.0.0.1:8000/"

    @classmethod
    def setUpClass(cls):
        cls.app = appbuilder.build_desktop_browser("chrome")
        cls.app.goto_url(cls.TEST_URL)

    def test_browser_type(self):
        self.assertEqual(self.app.get_browser_type(), BrowserTypes.CHROME)
        self.assertEqual(self.app.baseurl, self.TEST_URL)

    def test_action_textinput(self):
        txt_input = self.app.get_actions().textinput(By.NAME, "firstname")
        self.assertEqual(txt_input.get_value(), "")
        txt_input.set_value("something")
        self.assertEqual(txt_input.get_value(), "something")

    # def test_action_button(self):
    #     raise NotImplementedError

    def test_action_checkbox(self):
        agree_chk = self.app.get_actions().checkbox(By.NAME, "agree")
        self.assertFalse(agree_chk.is_checked())
        agree_chk.check()
        self.assertTrue(agree_chk.is_checked())
        agree_chk.uncheck()
        self.assertFalse(agree_chk.is_checked())
        agree_chk.set(CheckboxState.CHECKED)
        self.assertTrue(agree_chk.is_checked())

    def test_action_image(self):
        good_image = self.app.get_actions().image(By.XPATH, "//img[@alt='valid image']")
        broken_image = self.app.get_actions().image(By.XPATH, "//img[@alt='broken image']")
        self.assertTrue(good_image.is_image_loaded())
        self.assertFalse(broken_image.is_image_loaded())
        self.assertEqual(good_image.get_src(), self.TEST_URL + "img/avatar-blank.jpg")
        self.assertEqual(good_image.get_width(), '160')
        self.assertEqual(good_image.get_height(), '160')

    def test_action_radiobutton(self):
        male_radiobtn = self.app.get_actions().radiobutton(By.CSS_SELECTOR,
                                                           "body > form > p.male > label > input[type='radio']")
        female_radiobtn = self.app.get_actions().radiobutton(By.CSS_SELECTOR,
                                                             "body > form > p.female > label > input[type='radio']")
        self.assertTrue(male_radiobtn.is_selected())
        self.assertFalse(female_radiobtn.is_selected())
        female_radiobtn.click()
        self.assertFalse(male_radiobtn.is_selected())
        self.assertTrue(female_radiobtn.is_selected())

    def test_action_select(self):
        dropdown = self.app.get_actions().selectlist(By.CLASS_NAME, "numbers")
        self.assertEqual(dropdown.get_options_count(), 3)
        self.assertEqual(dropdown.get_selected_text(), "One")
        dropdown.select_by_index(2)
        self.assertEqual(dropdown.get_selected_text(), "Three")

    # def test_action_table(self):
    #     raise NotImplementedError

    def test_action_textlink(self):
        valid_link = self.app.get_actions().textlink(By.PARTIAL_LINK_TEXT, "Valid link")
        self.assertEqual(valid_link.get_href(), self.TEST_URL + "img/avatar-blank.jpg")

    def test_action_text(self):
        intro_txt = self.app.get_actions().text(By.ID, "introduction")
        self.assertEqual(intro_txt.get_text(), "Introductory text")

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()

if __name__ == "__main__":
    unittest.main()

