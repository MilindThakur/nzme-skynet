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
        self.assertEqual(len(broken_images), 2, "Expected 2 broken images, found: " + str(len(broken_images)))

    def test_link_validation(self):
        broken_links = v._validate_links_on_url(self.BROKEN_LINK_URL, driver=self.driver)
        self.assertEqual(len(broken_links), 3, "Expected 3 broken links, found: " + str(len(broken_links)))

    def test_javascript_validation(self):
        js_errors = v._validate_js_error_on_url(self.JAVASCRIPT_ERROR_URL, driver=self.driver)
        self.assertEqual(len(js_errors), 1, "Expected 1 js error, found: " + str(len(js_errors)))

    def test_all_validation(self):
        errors = v.validate_all(self.BROKEN_IMAGE_URL)
        self.assertEqual(len(errors), 2, "Expected 2 errors, found: " + str(len(errors)))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()