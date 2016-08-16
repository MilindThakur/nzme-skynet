# coding=utf-8
import os
import shutil
import unittest

from nzme_skynet.core.layout.layoutscreenshot import LayoutScreenshot


class LayoutTestCase(unittest.TestCase):
    SCREENSHOT_PATH = os.path.abspath('.') + "/%s" % "screenshot"
    CUR_DIR = os.path.dirname(__file__)

    def setUp(self):
        if os.path.exists(self.SCREENSHOT_PATH):
            shutil.rmtree(self.SCREENSHOT_PATH)

    def test_layout_devices(self):
        sc = LayoutScreenshot(os.path.join(self.CUR_DIR,"testdata/urls.json"),
                              os.path.join(self.CUR_DIR,"testdata/devices.json"))
        sc.take_screenshot()
        self.assertEqual(os.path.exists(sc.SCREENSHOT_DIR_PATH), True, "Failed to create screenshot directory")
        self.assertEqual(len(os.listdir(sc.SCREENSHOT_DIR_PATH)) > 0, True, "Failed to create snapshots")

    def tearDown(self):
        if os.path.exists(self.SCREENSHOT_PATH):
            shutil.rmtree(self.SCREENSHOT_PATH)

if __name__ == "__main__":
    unittest.main()