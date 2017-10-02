# coding=utf-8
import unittest

from selenium.webdriver.common.by import By

from nzme_skynet.core.actions.enums.checkboxstates import CheckboxState
from nzme_skynet.core.driver.builder import build_desktop_browser
from nzme_skynet.core.driver.drivertypes import DriverTypes


class ActionsTestCase(unittest.TestCase):
    TEST_URL = "http://127.0.0.1:8000/"

    @classmethod
    def setUpClass(cls):
        cap = {
            "type": "phantomjs",
            "platform": 'LINUX',
            "version": '',
            "javascriptEnabled": True
        }
        cls.app = build_desktop_browser(cap)
        cls.app.goto_url(cls.TEST_URL, relative=False)

    def test_browser_type(self):
        self.assertEqual(self.app.get_browser_type(), DriverTypes.PHANTOM_JS)
        self.assertEqual(self.app.baseurl, self.TEST_URL)

    def test_get_window_handles(self):
        self.assertNotEqual(None, self.app.get_window_handles())
        self.assertEqual(1, len(self.app.get_window_handles()))

    def test_switch_window_handles(self):
        new_page_text_link = self.app.action.textlink(By.LINK_TEXT, "new_page")
        new_page_handle = self.app.get_window_handles()[0]
        new_page_text_link.click()
        self.assertEqual(2, len(self.app.get_window_handles()))
        self.app.switch_to_newest_window()
        self.assertNotEqual(new_page_handle, self.app.get_current_window_handle())
        self.app.driver.close()
        self.assertEqual(1, len(self.app.get_window_handles()))
        self.app.switch_to_oldest_window()
        self.assertEqual(new_page_handle, self.app.get_current_window_handle())

    def test_action_textinput(self):
        txt_input = self.app.action.textinput(By.NAME, "firstname")
        self.assertEqual(txt_input.get_value(), "")
        txt_input.set_value("something")
        self.assertEqual(txt_input.get_value(), "something")

    def test_action_button(self):
        submit_btn = self.app.action.button(By.NAME, "submit")
        self.assertEqual(submit_btn.get_text(), "Submit")

    def test_action_checkbox(self):
        agree_chk = self.app.action.checkbox(By.NAME, "agree")
        self.assertFalse(agree_chk.is_checked())
        agree_chk.check()
        self.assertTrue(agree_chk.is_checked())
        agree_chk.uncheck()
        self.assertFalse(agree_chk.is_checked())
        agree_chk.set(CheckboxState.CHECKED)
        self.assertTrue(agree_chk.is_checked())

    def test_action_image(self):
        good_image = self.app.action.image(By.XPATH, "//img[@alt='valid image']")
        broken_image = self.app.action.image(By.XPATH, "//img[@alt='broken image']")
        self.assertTrue(good_image.is_image_loaded())
        self.assertFalse(broken_image.is_image_loaded())
        self.assertEqual(good_image.get_src(), self.TEST_URL + "img/avatar-blank.jpg")
        self.assertEqual(good_image.get_width(), '160')
        self.assertEqual(good_image.get_height(), '160')

    def test_action_radiobutton(self):
        male_radiobtn = self.app.action.radiobutton(By.CSS_SELECTOR,
                                                           "body > form > p.male > label > input[type='radio']")
        female_radiobtn = self.app.action.radiobutton(By.CSS_SELECTOR,
                                                             "body > form > p.female > label > input[type='radio']")
        self.assertTrue(male_radiobtn.is_selected())
        self.assertFalse(female_radiobtn.is_selected())
        female_radiobtn.click()
        self.assertFalse(male_radiobtn.is_selected())
        self.assertTrue(female_radiobtn.is_selected())

    def test_action_select(self):
        dropdown = self.app.action.selectlist(By.CLASS_NAME, "numbers")
        self.assertEqual(dropdown.get_options_count(), 3)
        self.assertEqual(dropdown.get_selected_text(), "One")
        dropdown.select_by_index(2)
        self.assertEqual(dropdown.get_selected_text(), "Three")

    def test_action_textlink(self):
        valid_link = self.app.action.textlink(By.PARTIAL_LINK_TEXT, "Valid link")
        self.assertEqual(valid_link.get_href(), self.TEST_URL + "img/avatar-blank.jpg")

    def test_action_text(self):
        intro_txt = self.app.action.text(By.ID, "introduction")
        self.assertEqual(intro_txt.get_text(), "Introductory text")

    def test_action_element(self):
        elem = self.app.action.element(By.CLASS_NAME, "textInput")
        self.assertEqual(elem.get_attr("value"), "Sample Text")

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()


if __name__ == "__main__":
    unittest.main()

