# -*- coding: utf-8 -*-
from nzme_skynet.core.pageobject.basewebpage import BaseWebPage
from selenium.webdriver.common.by import By
import unittest
from nzme_skynet.core.driver.builder import build_docker_browser


class GoogleHomePage(BaseWebPage):
    page_url = "https://www.google.co.nz/"

    def __init__(self, driver):
        super(GoogleHomePage, self).__init__(driver)
        self.search_input = self.locate.textinput(By.NAME, 'q')
        self.submit_search_btn = self.locate.button(By.NAME, 'btnK')

    def search(self, string):
        self.search_input.set_value(string)
        self.submit_search_btn.click()


class GoogleSearchResultPage(BaseWebPage):

    def __init__(self, driver):
        super(GoogleSearchResultPage, self).__init__(driver)
        self.search_result_container = self.locate.element(By.ID, 'rso')

    def get_result_url(self, index):
        return self.search_result_container.find_sub_elements(By.TAG_NAME, "cite")[index-1].text


class POValidation(unittest.TestCase):
    DOCKER_SELENIUM_URL = "http://localhost:4444/wd/hub"

    def setUp(self):
        cap = {
            "browserName": "chrome",
            "platform": 'LINUX',
            "version": '',
            "javascriptEnabled": True
        }
        self.driver = build_docker_browser(self.DOCKER_SELENIUM_URL, cap)

    def test_WebPOCreation(self):
        ghomepage = GoogleHomePage(self.driver)
        assert isinstance(ghomepage, BaseWebPage) is True
        ghomepage.goto(relative=False)
        assert "google.co.nz" in ghomepage.page.get_current_url(), "Failed to match browser url"
        ghomepage.search('nzme')
        gresultpage = GoogleSearchResultPage(self.driver)
        assert isinstance(gresultpage, BaseWebPage) is True
        assert gresultpage.page_url is None
        gresultpage.search_result_container.will_be_visible()
        first_result_url = gresultpage.get_result_url(1)
        assert "www.nzme.co.nz/" in first_result_url, "Unexpected {0} found in first result".format(first_result_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
