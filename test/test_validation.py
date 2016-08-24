# coding=utf-8
import os
import shutil
import unittest
from nzme_skynet.core.layout.validation import Validation


class ValidationTestCase(unittest.TestCase):
    CUR_DIR = os.path.dirname(__file__)
    DEFAULT_RESULTS_FOLDER_PATH = os.path.abspath('.') + "/%s" % "ValidationResults"
    CUSTOM_RESULTS_FOLDER_PATH = os.path.abspath('.') + "/%s" % "Results"


    def test_validate_no_urls_file(self):
        im = Validation(os.path.join(self.CUR_DIR, "testdata/nourl.json"))
        im.validate()
        self.assertTrue(not os.path.exists(self.DEFAULT_RESULTS_FOLDER_PATH),
                        "Not expecting results folder path to be created")

    def test_validate_good_images_file(self):
        im = Validation(os.path.join(self.CUR_DIR, "testdata/goodimages.json"))
        im.validate()
        self.assertFalse(os.path.exists(self.DEFAULT_RESULTS_FOLDER_PATH),
                        "Not expecting results folder path to be created")

    def test_validate_good_links_file(self):
        im = Validation(os.path.join(self.CUR_DIR, "testdata/goodlinks.json"))
        im.validate()
        self.assertFalse(os.path.exists(self.DEFAULT_RESULTS_FOLDER_PATH),
                         "Not expecting results folder path to be created")
    #
    def test_validate_broken_images_file(self):
        im = Validation(os.path.join(self.CUR_DIR,"testdata/brokenimages.json"))
        im.validate()
        self.assertTrue(os.path.exists(self.DEFAULT_RESULTS_FOLDER_PATH), "Failed to create default results folder path")
        self.assertTrue(len(os.listdir(self.DEFAULT_RESULTS_FOLDER_PATH)) == 1, "Failed to create result files")
        self.assertTrue(os.stat(self.DEFAULT_RESULTS_FOLDER_PATH + "/" +
                         os.listdir(self.DEFAULT_RESULTS_FOLDER_PATH)[0]).st_size != 0,
                         "Expecting an invalid result for the test url")

    def test_validate_broken_links_file(self):
        im = Validation(os.path.join(self.CUR_DIR, "testdata/brokenlinks.json"))
        im.validate()
        self.assertTrue(os.path.exists(self.DEFAULT_RESULTS_FOLDER_PATH), "Failed to create default results folder path")
        self.assertTrue(len(os.listdir(self.DEFAULT_RESULTS_FOLDER_PATH)) == 1, "Failed to create result files")
        self.assertTrue(os.stat(self.DEFAULT_RESULTS_FOLDER_PATH + "/" +
                         os.listdir(self.DEFAULT_RESULTS_FOLDER_PATH)[0]).st_size != 0,
                         "Expecting an invalid result for the test url")

    def test_validate_customresultsfolder(self):
        im = Validation(os.path.join(self.CUR_DIR, "testdata/brokenimages.json"), custom_results_path=self.CUSTOM_RESULTS_FOLDER_PATH)
        im.validate()
        self.assertTrue(os.path.exists(self.CUSTOM_RESULTS_FOLDER_PATH), "Failed to create default results folder path")
        self.assertTrue(len(os.listdir(self.CUSTOM_RESULTS_FOLDER_PATH)) == 1, "Failed to create result files")
        self.assertTrue(os.stat(self.CUSTOM_RESULTS_FOLDER_PATH + "/" +
                                os.listdir(self.CUSTOM_RESULTS_FOLDER_PATH)[0]).st_size != 0,
                        "Expecting an invalid result for the test url")


    def tearDown(self):
        if os.path.exists(self.CUSTOM_RESULTS_FOLDER_PATH):
            shutil.rmtree(self.CUSTOM_RESULTS_FOLDER_PATH)
        if os.path.exists(self.DEFAULT_RESULTS_FOLDER_PATH):
            shutil.rmtree(self.DEFAULT_RESULTS_FOLDER_PATH)

if __name__ == "__main__":
    unittest.main()
