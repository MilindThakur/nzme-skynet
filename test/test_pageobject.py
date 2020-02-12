# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver.common.by import By

from nzme_skynet.core.controls.textinput import TextInput
from nzme_skynet.core.controls.button import Button
from nzme_skynet.core.controls.element import Element
from nzme_skynet.core.driver.driverregistry import DriverRegistry
from nzme_skynet.core.pageobject.basewebpage import BaseWebPage
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes


class GoogleHomePage(BaseWebPage):
    page_url = "https://www.google.co.nz/"
    search_input = TextInput(By.NAME, 'q')
    submit_search_btn = Button(By.NAME, 'btnK')

    def search(self, string):
        self.search_input.set_value(string)
        self.submit_search_btn.click()


class GoogleSearchResultPage(BaseWebPage):
    search_result_container = Element(By.ID, 'rso')

    def get_result_url(self, index):
        return self.search_result_container.find_sub_elements(By.TAG_NAME, "cite")[index-1].text


class POValidation(unittest.TestCase):

    def setUp(self):
        DriverRegistry.register_driver(
            driver_type=DriverTypes.CHROME, local=False)

    def test_web_page_object_creation(self):
        ghomepage = GoogleHomePage()
        assert isinstance(ghomepage, BaseWebPage) is True
        ghomepage.goto(absolute=True)
        assert "google.co.nz"in ghomepage.driver.current_url, "Failed to match browser url"
        ghomepage.search('nzme')
        gresultpage = GoogleSearchResultPage()
        assert isinstance(gresultpage, BaseWebPage) is True
        assert gresultpage.page_url is None
        gresultpage.search_result_container.will_be_visible()
        first_result_url = gresultpage.get_result_url(1)
        assert "www.nzme.co.nz" in first_result_url, "Unexpected {0} found in first result".format(
            first_result_url)

    def tearDown(self):
        DriverRegistry.deregister_driver()


if __name__ == "__main__":
    unittest.main()
