# coding=utf-8
import os
import shutil
import unittest

from nzme_skynet.core.layout.layoutscreenshot import LayoutScreenshot


class LayoutTestCase(unittest.TestCase):
    SCREENSHOT_PATH = os.path.abspath('.') + "/%s" % "screenshot"
    CUR_DIR = os.path.dirname(__file__)
    CUSTOM_DOWNLOAD_FOLDER = "./results"

    def setUp(self):
        if os.path.exists(self.SCREENSHOT_PATH):
            shutil.rmtree(self.SCREENSHOT_PATH)

    def test_screenshot_with_default_download_folder(self):
        sc = LayoutScreenshot(os.path.join(self.CUR_DIR,"testdata/urls.json"), "iPhone_4,iPhone_5")
        sc.take_screenshot()
        self.assertEqual(os.path.exists(self.SCREENSHOT_PATH), True, "Failed to create screenshot directory")
        self.assertEqual(len(os.listdir(self.SCREENSHOT_PATH)) == 2, True, "Failed to create snapshots")

    def test_screenshot_with_custom_download_folder(self):
        sc = LayoutScreenshot(os.path.join(self.CUR_DIR, "testdata/urls.json"), "iPhone_6,iPad_4",
                              self.CUSTOM_DOWNLOAD_FOLDER)
        sc.take_screenshot()
        self.assertEqual(os.path.exists(self.CUSTOM_DOWNLOAD_FOLDER), True, "Failed to create customer screenshot directory")
        self.assertEqual(len(os.listdir(self.CUSTOM_DOWNLOAD_FOLDER)) == 2, True, "Failed to create snapshots")

    def tearDown(self):
        if os.path.exists(self.SCREENSHOT_PATH):
            shutil.rmtree(self.SCREENSHOT_PATH)
        if os.path.exists(self.CUSTOM_DOWNLOAD_FOLDER):
            shutil.rmtree(self.CUSTOM_DOWNLOAD_FOLDER)

if __name__ == "__main__":
    unittest.main()