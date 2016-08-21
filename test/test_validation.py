# coding=utf-8
import unittest
from skynet.core.layout.validation import Validation
from skynet.core.browsers.localbrowserbuilder import LocalBrowserBuilder



class ValidationTestCase(unittest.TestCase):




    def setUp(self):
      pass


    def test_validation_default(self):
        urls_path = "./testdata/urls2.json"
        im = Validation(urls_path)
        a = im.validate()
        print a


    def test_validation_nofile(self):
        urls_path = ""
        im = Validation(urls_path)
        a = im.validate()
        print a

    def test_validation_filepath(self):
        urls_path = "/home/donnam/Documents/urls2.json"
        im = Validation(urls_path)
        a = im.validate()
        print a


    def test_validation_resultspath(self):
        urls_path = "./testdata/urls2.json"
        path = "/home/donnam/Docments"
        im = Validation(urls_path, results_path=path)
        a = im.validate()
        print a



    def tearDown(self):
        pass

