# coding=utf-8
import unittest

import nzme_skynet.core.layout.urlvalidation as v


class UrlValidationTestCase(unittest.TestCase):

    BROKEN_URL = "htt://www.nzherald.co.nz"
    TEST_URL = "http://127.0.0.1:8000/"

    def test_broken_url_validation(self):
        broken_images = v.validate_images(self.BROKEN_URL)
        self.assertRaises(Exception, broken_images)

    def test_image_validation(self):
        broken_images = v.validate_images(self.TEST_URL)
        self.assertEqual(len(broken_images), 1, "Expected 1 broken img, found: " + str(len(broken_images)))

    def test_link_validation(self):
        broken_links = v.validate_links(self.TEST_URL)
        self.assertEqual(len(broken_links), 1, "Expected 1 broken links, found: " + str(broken_links))

    def test_javascript_validation(self):
        js_errors = v.validate_js_error(self.TEST_URL)
        self.assertEqual(len(js_errors), 1, "Expected 1 js error, found: " + str(len(js_errors)))

    def test_all_validation(self):
        errors = v.validate_all(self.TEST_URL)
        self.assertEqual(len(errors), 3, "Expected 3 errors, found: " + str(errors))


if __name__ == "__main__":
    unittest.main()
