# coding=utf-8
import unittest
import nzme_skynet.core.layout.urlvalidation as v

class UrlValidationTestCase(unittest.TestCase):

    BROKEN_IMAGE_URL = "https://the-internet.herokuapp.com/broken_images"
    BROKEN_LINK_URL = "https://the-internet.herokuapp.com/status_codes"
    JAVASCRIPT_ERROR_URL = "http://webdriverjsdemo.github.io/error/"

    def setUp(self):
        self.driver = v.create_webdriver_instance()

    def test_image_validation(self):
        broken_images = v._validate_images_on_url(self.BROKEN_IMAGE_URL, driver=self.driver)
        self.assertEqual(len(broken_images), 2, "Expected 2 broken images")

    def test_link_validation(self):
        broken_links = v._validate_links_on_url(self.BROKEN_LINK_URL, driver=self.driver)
        self.assertEqual(len(broken_links), 3, "Expected 3 broken links")

    def test_javascript_validation(self):
        js_errors = v._validate_js_error_on_url(self.JAVASCRIPT_ERROR_URL, driver=self.driver)
        self.assertEqual(len(js_errors), 1, "Expected 1 js error")

    def test_all_validation(self):
        errors = v.validate_all(self.BROKEN_IMAGE_URL)
        self.assertEqual(len(errors), 2, "Expected 2 errors")

    def test_all_validation_urls_list(self):
        URL_LIST = [self.BROKEN_IMAGE_URL, self.BROKEN_LINK_URL, self.JAVASCRIPT_ERROR_URL]
        result_dict = {}
        for url in URL_LIST:
            errors = v.validate_all(url)
            if errors:
                result_dict[url] = errors
        self.assertEqual(len(result_dict), 3, "Expected 3 url errors")
        self.assertTrue(result_dict.has_key(self.BROKEN_IMAGE_URL), "Expected broken image url")
        self.assertTrue(result_dict.has_key(self.BROKEN_LINK_URL), "Expected broken link url")
        self.assertTrue(result_dict.has_key(self.JAVASCRIPT_ERROR_URL), "Expected js error url")
        self.assertEqual(len(result_dict[self.BROKEN_IMAGE_URL]), 2, "Expected 2 broken images")
        self.assertEqual(len(result_dict[self.BROKEN_LINK_URL]), 3, "Expected 3 broken links")
        self.assertEqual(len(result_dict[self.JAVASCRIPT_ERROR_URL]), 1, "Expected 1 js error")

    def tearDown(self):
        self.driver.quit()