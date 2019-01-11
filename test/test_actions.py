# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver.common.by import By

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
    TEST_URL = "http://the-internet.herokuapp.com/"

    @classmethod
    def setUpClass(cls):
        DriverRegistry.register_driver(DriverTypes.CHROMEHEADLESS, local=False)
        cls.driver = DriverRegistry.get_driver()
        cls.driver.goto_url(cls.TEST_URL, absolute=True)

    def test_browser_type(self):
        self.assertEqual(self.driver.name, DriverTypes.CHROME)
        # self.assertEqual(self.app.baseurl, self.TEST_URL)

    def test_get_window_handles(self):
        self.assertIsNotNone(self.driver.window_handles)
        self.assertEqual(1, len(self.driver.window_handles))

    def test_switch_window_handles(self):
        multiple_window_text_link = TextLink(by=By.LINK_TEXT, locator="Multiple Windows")
        multiple_window_text_link.click()
        click_here_text_link = TextLink(by=By.LINK_TEXT, locator="Click Here")
        new_page_handle = self.driver.window_handles[0]
        click_here_text_link.click()
        self.assertEqual(2, len(self.driver.window_handles))
        self.driver.switch_to_newest_window()
        self.assertNotEqual(new_page_handle, self.driver.window_handles)
        self.driver.close()
        self.assertEqual(1, len(self.driver.window_handles))
        self.driver.switch_to_oldest_window()
        self.assertEqual(new_page_handle, self.driver.window_handles[0])

    def test_action_textinput(self):
        form_authentication = TextLink(by=By.LINK_TEXT, locator="Form Authentication")
        form_authentication.click()
        txt_input = TextInput(By.NAME, "username")
        self.assertEqual(txt_input.value, "")
        txt_input.set_value("tomsmith")
        self.assertEqual(txt_input.value, "tomsmith")

    def test_action_button(self):
        form_authentication = TextLink(by=By.LINK_TEXT, locator="Form Authentication")
        form_authentication.click()
        submit_btn = Button(By.CLASS_NAME, "radius")
        self.assertEqual(submit_btn.text, "Login")


    def test_action_checkbox(self):
        checkboxes = TextLink(by=By.LINK_TEXT, locator="Checkboxes")
        checkboxes.click()
        agree_chk = Checkbox(By.XPATH, '//*[@id="checkboxes"]/input[1]')
        self.assertFalse(agree_chk.is_checked())
        agree_chk.check()
        self.assertTrue(agree_chk.is_checked())
        agree_chk.uncheck()
        self.assertFalse(agree_chk.is_checked())
        agree_chk.set(CheckboxState.CHECKED)
        self.assertTrue(agree_chk.is_checked())

    def test_action_image(self):
        image_link = TextLink(by=By.LINK_TEXT, locator="Broken Images")
        image_link.click()
        good_image = Image(By.XPATH, "//*[@class='example']/img[3]")
        broken_image = Image(By.XPATH, "//*[@class='example']/img[1]")
        self.assertTrue(good_image.is_image_loaded())
        self.assertFalse(broken_image.is_image_loaded())
        self.assertEqual(good_image.src, self.TEST_URL + "img/avatar-blank.jpg")
        self.assertEqual(good_image.width, '120')
        self.assertEqual(good_image.height, '90')

    def test_action_select(self):
        dropdown_link = TextLink(by=By.LINK_TEXT, locator="Dropdown")
        dropdown_link.click()
        dropdown = SelectElem(By.ID, "dropdown")
        self.assertEqual(dropdown.get_options_count(), 3)
        self.assertEqual(dropdown.get_selected_text(), "Please select an option")
        dropdown.select_by_index(2)
        self.assertEqual(dropdown.get_selected_text(), "Option 2")

    def test_action_textlink(self):
        redirect_link = TextLink(By.PARTIAL_LINK_TEXT, "Redirect Link")
        self.assertEqual(redirect_link.href, self.TEST_URL + "redirector")

    def test_action_text(self):
        heading_txt = Text(By.CLASS_NAME, "heading")
        self.assertEqual(heading_txt.text, "Welcome to the-internet")

    def test_action_element(self):
        dropdown_link = TextLink(by=By.LINK_TEXT, locator="Dropdown")
        dropdown_link.click()
        elem = Element(By.ID, "dropdown")
        elem1 = Element(By.XPATH, ".//*[@id='dropdown']/option[2]")
        self.assertEqual(elem1.get_attribute("value"), "1")

    def tearDown(cls):
        cls.driver.goto_url(cls.TEST_URL, absolute=True)

    @classmethod
    def tearDownClass(cls):
        DriverRegistry.deregister_driver()


if __name__ == "__main__":
    unittest.main()

