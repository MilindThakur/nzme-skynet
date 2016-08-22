# coding=utf-8
import os
import unittest
from nzme_skynet.core.layout.validation import Validation




class ValidationTestCase(unittest.TestCase):

    SCREENSHOT_PATH = os.path.abspath('.') + "/%s" % "Validation"
    CUR_DIR = os.path.dirname(__file__)
    CUSTOM_DOWNLOAD_FOLDER = "./valresults"




    def setUp(self):
      pass


    def test_validation_default(self):
        urls_path = os.path.join(self.CUR_DIR, "testdata/urls2.json")
        im = Validation(urls_path)
        a = im.validate()
        print a


    def test_validation_nofile(self):

        urls_path = ""
        try:
            im = Validation(urls_path)
            a = im.validate()
        except IOError, e:
            if e.errno == 2:
                print e
            else:
                raise


    def test_validation_resultspath(self):
        urls_path = os.path.join(self.CUR_DIR, "testdata/urls2.json")
        im = Validation(urls_path, results_path=self.CUSTOM_DOWNLOAD_FOLDER)
        a = im.validate()
        print a



    def tearDown(self):
        pass

