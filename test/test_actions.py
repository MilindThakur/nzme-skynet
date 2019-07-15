# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from nzme_skynet.core.controls.button import Button
from nzme_skynet.core.controls.checkbox import Checkbox
from nzme_skynet.core.controls.radiobutton import RadioButton
from nzme_skynet.core.controls.select import SelectElem
from nzme_skynet.core.controls.textinput import TextInput
from nzme_skynet.core.controls.textlink import TextLink
from nzme_skynet.core.controls.image import Image
from nzme_skynet.core.controls.text import Text
from nzme_skynet.core.controls.element import Element
from nzme_skynet.core.controls.enums.checkboxstates import CheckboxState
from nzme_skynet.core.driver.driverregistry import DriverRegistry
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes


class ActionsTestCase(unittest.TestCase):
    TEST_URL = "http://testserver:8080/"

    @classmethod
    def setUpClass(cls):
        DriverRegistry.register_driver(DriverTypes.CHROME, local=False)
        cls.driver = DriverRegistry.get_driver()
        cls.driver.goto_url(cls.TEST_URL, absolute=True)

    def test_browser_type(self):
        self.assertEqual(self.driver.name, DriverTypes.CHROME)
        # self.assertEqual(self.app.baseurl, self.TEST_URL)

    def test_get_window_handles(self):
        self.assertIsNotNone(self.driver.window_handles)
        self.assertEqual(1, len(self.driver.window_handles))

    def test_switch_window_handles(self):
        new_page_text_link = TextLink(by=By.LINK_TEXT, locator="new_page")
        new_page_handle = self.driver.window_handles[0]
        new_page_text_link.click()
        self.assertEqual(2, len(self.driver.window_handles))
        self.driver.switch_to_newest_window()
        self.assertNotEqual(new_page_handle, self.driver.window_handles)
        self.driver.close()
        self.assertEqual(1, len(self.driver.window_handles))
        self.driver.switch_to_oldest_window()
        self.assertEqual(new_page_handle, self.driver.window_handles[0])

    def test_action_textinput(self):
        txt_input = TextInput(By.NAME, "firstname", index=1)
        self.assertEqual(txt_input.value, "")
        txt_input.set_value("something")
        self.assertEqual(txt_input.value, "something")

    def test_action_button(self):
        submit_btn = Button(By.NAME, "submit")
        self.assertEqual(submit_btn.text, "Submit")

    def test_action_checkbox(self):
        agree_chk = Checkbox(By.NAME, "agree")
        self.assertFalse(agree_chk.is_checked())
        agree_chk.check()
        self.assertTrue(agree_chk.is_checked())
        agree_chk.uncheck()
        self.assertFalse(agree_chk.is_checked())
        agree_chk.set(CheckboxState.CHECKED)
        self.assertTrue(agree_chk.is_checked())

    def test_action_image(self):
        good_image = Image(By.XPATH, "//img[@alt='valid image']")
        broken_image = Image(By.XPATH, "//img[@alt='broken image']")
        self.assertTrue(good_image.is_image_loaded())
        self.assertFalse(broken_image.is_image_loaded())
        self.assertEqual(good_image.src, self.TEST_URL +
                         "img/avatar-blank.jpg")
        self.assertEqual(good_image.width, '160')
        self.assertEqual(good_image.height, '160')

    def test_action_radiobutton(self):
        male_radiobtn = RadioButton(
            By.CSS_SELECTOR, "body > form > p.male > label > input[type='radio']")
        female_radiobtn = RadioButton(
            By.CSS_SELECTOR, "body > form > p.female > label > input[type='radio']")
        self.assertTrue(male_radiobtn.is_selected())
        self.assertFalse(female_radiobtn.is_selected())
        female_radiobtn.click()
        self.assertFalse(male_radiobtn.is_selected())
        self.assertTrue(female_radiobtn.is_selected())

    def test_action_select(self):
        dropdown = SelectElem(By.CLASS_NAME, "numbers")
        self.assertEqual(dropdown.get_options_count(), 3)
        self.assertEqual(dropdown.get_selected_text(), "One")
        dropdown.select_by_index(2)
        self.assertEqual(dropdown.get_selected_text(), "Three")

    def test_action_textlink(self):
        valid_link = TextLink(By.PARTIAL_LINK_TEXT, "Valid link")
        self.assertEqual(valid_link.href, self.TEST_URL +
                         "img/avatar-blank.jpg")

    def test_action_text(self):
        intro_txt = Text(By.ID, "introduction")
        self.assertEqual(intro_txt.text, "Introductory text")

    def test_action_element(self):
        elem = Element(By.CLASS_NAME, "textInput")
        self.assertEqual(elem.get_attribute("value"), "Sample Text")

    def test_base_element_methods(self):
        elem1 = Text(By.NAME, "firstname")
        self.assertTrue(isinstance(elem1.element, WebElement))
        elem2 = TextInput(By.NAME, "firstname", index=1)
        self.assertTrue(isinstance(elem2.element, WebElement))
        elem3 = TextInput(By.TAG_NAME, "input", parent=(By.CLASS_NAME, "male"))
        self.assertTrue(isinstance(elem3.element, WebElement))
        elem5 = TextInput(By.TAG_NAME, "input", parent=Element(By.CLASS_NAME, "male"))
        self.assertTrue(isinstance(elem5.element, WebElement))
        elem6 = TextInput(By.TAG_NAME, "input", parent=Element(By.CLASS_NAME, "male"), index=1)
        self.assertTrue(isinstance(elem6.element, WebElement))

    @classmethod
    def tearDownClass(cls):
        DriverRegistry.deregister_driver()


if __name__ == "__main__":
    unittest.main()
