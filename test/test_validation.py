# coding=utf-8
import os
import shutil
import unittest
from nzme_skynet.core.layout.validation import Validation


class ValidationTestCase(unittest.TestCase):
    CUR_DIR = os.path.dirname(__file__)
    DEFAULT_RESULTS_FOLDER_PATH = os.path.abspath('./') + "/%s" % "ValidationResults"
    CUSTOM_RESULTS_FOLDER_PATH = os.path.abspath('./') + "/%s" % "Results"

    def setUp(self):
        if os.path.exists(self.CUSTOM_RESULTS_FOLDER_PATH):
            shutil.rmtree(self.CUSTOM_RESULTS_FOLDER_PATH)
        if os.path.exists(self.DEFAULT_RESULTS_FOLDER_PATH):
            shutil.rmtree(self.DEFAULT_RESULTS_FOLDER_PATH)

    def test_validate_broken_images(self):
        image = Validation(os.path.join(self.CUR_DIR, "testdata/brokenimages.json"))
        imagelist = image.validate_images_on_url()
        self.assertNotEqual(len(imagelist), 0, "Expected broken image list to be returned but empty")

    def test_validate_good_images(self):
        image = Validation(os.path.join(self.CUR_DIR, "testdata/goodimages.json"))
        imagelist = image.validate_images_on_url()
        self.assertListEqual(imagelist, [], 'Expected empty broken images list but returned items')

    def test_validate_broken_javascript(self):
        js = Validation(os.path.join(self.CUR_DIR,"testdata/brokenjs.json"))
        jslist = js.validate_javascript_on_url()
        self.assertNotEqual(len(jslist), 0, "Expected js errors list to be returned but empty")

    def test_validate_good_javascript(self):
        js = Validation(os.path.join(self.CUR_DIR, "testdata/goodjs.json"))
        jslist = js.validate_javascript_on_url()
        self.assertListEqual(jslist, [], 'Expected empty js errors list but returned items')

    def test_validate_good_links(self):
        links = Validation(os.path.join(self.CUR_DIR, "testdata/goodlinks.json"))
        linkslist = links.validate_links_on_url()
        self.assertListEqual(linkslist, [], 'Expected empty broken links list but returned items')

    def test_validate_all(self):
        im = Validation(os.path.join(self.CUR_DIR,"testdata/brokenimages.json"))
        im.validateall()
        self.assertTrue(os.path.exists(self.DEFAULT_RESULTS_FOLDER_PATH), "Failed to create default results folder path")
        self.assertTrue(len(os.listdir(self.DEFAULT_RESULTS_FOLDER_PATH)) == 1, "Failed to create result files")
        self.assertGreater(os.stat(self.DEFAULT_RESULTS_FOLDER_PATH + "/" +
                     os.listdir(self.DEFAULT_RESULTS_FOLDER_PATH)[0]).st_size, 0,
                     "Expecting an invalid result for the test url")

    def test_validate_customresultsfolder(self):
        im = Validation(os.path.join(self.CUR_DIR, "testdata/brokenimages.json"), custom_results_path=self.CUSTOM_RESULTS_FOLDER_PATH)
        im.validateall()
        self.assertTrue(os.path.exists(self.CUSTOM_RESULTS_FOLDER_PATH), "Failed to create default results folder path")
        self.assertTrue(len(os.listdir(self.CUSTOM_RESULTS_FOLDER_PATH)) == 1, "Failed to create result files")
        self.assertGreater(os.stat(self.CUSTOM_RESULTS_FOLDER_PATH + "/" +
                                os.listdir(self.CUSTOM_RESULTS_FOLDER_PATH)[0]).st_size, 0,
                        "Expecting an invalid result for the test url")

    def test_validate_no_urls_file(self):
        im = Validation(os.path.join(self.CUR_DIR, "testdata/nourl.json"))
        im.validateall()
        self.assertFalse(os.path.exists(self.DEFAULT_RESULTS_FOLDER_PATH),
                         "Not expecting results folder path to be created")

    def tearDown(self):
        if os.path.exists(self.CUSTOM_RESULTS_FOLDER_PATH):
            shutil.rmtree(self.CUSTOM_RESULTS_FOLDER_PATH)
        if os.path.exists(self.DEFAULT_RESULTS_FOLDER_PATH):
            shutil.rmtree(self.DEFAULT_RESULTS_FOLDER_PATH)

if __name__ == "__main__":
    unittest.main()
