# coding=utf-8
import unittest

import nzme_skynet.core.layout.urlvalidation as v


class UrlValidationTestCase(unittest.TestCase):

    BROKEN_URL = "htt://www.nzherald.co.nz"
    TEST_URL = "http://localhost:8000/"

    def setUp(self):
        self.driver = v.create_webdriver_instance()

    def test_broken_url_validation(self):
        broken_images = v._validate_images_on_url(self.BROKEN_URL, driver=self.driver)
        self.assertRaises(Exception, broken_images)

    def test_image_validation(self):
        broken_images = v._validate_images_on_url(self.TEST_URL, driver=self.driver)
        self.assertEqual(len(broken_images), 1, "Expected 1 broken img, found: " + str(len(broken_images)))

    def test_link_validation(self):
        broken_links = v._validate_links_on_url(self.TEST_URL, driver=self.driver)
        self.assertEqual(len(broken_links), 1, "Expected 1 broken links, found: " + str(broken_links))

    def test_javascript_validation(self):
        js_errors = v._validate_js_error_on_url(self.TEST_URL, driver=self.driver)
        self.assertEqual(len(js_errors), 1, "Expected 1 js error, found: " + str(len(js_errors)))

    def test_all_validation(self):
        errors = v.validate_all(self.TEST_URL)
        self.assertEqual(len(errors), 3, "Expected 3 errors, found: " + str(errors))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()