# coding=utf-8
import json
import os
from datetime import datetime

from skynet.core.browsers.localbrowserbuilder import LocalBrowserBuilder


class LayoutScreenshot(object):
    SCREENSHOT_DIR_NAME = "screenshot"
    SCREENSHOT_DIR_PATH = os.path.abspath('.') + "/%s" % SCREENSHOT_DIR_NAME

    def __init__(self, urls_path, devices_path):
        with open(urls_path, 'r') as urlf:
            self.urls_json = json.load(urlf)
        with open(devices_path, 'r') as devicesf:
            self.devices_json = json.load(devicesf)
        self._create_screenshot_folder()

    def _create_screenshot_folder(self):
        if not os.path.exists(self.SCREENSHOT_DIR_PATH):
            os.makedirs(self.SCREENSHOT_DIR_PATH)

    def take_screenshot(self):
        lb = LocalBrowserBuilder("phantomJS")
        browser = lb.build()
        for url in self.urls_json["urls"]:
            for devices in self.devices_json["supportDevices"]:
                for brand in devices["brands"]:
                    browser.set_window_size(brand["w"], brand["h"])
                    browser.goto_url(url["url"])
                    filename = "%s_%s_%s.png" % (url["name"].replace(" ", ""), brand["name"].replace(" ", ""),
                                                 datetime.now().strftime("%Y%m%d-%H%M%S"))
                    browser.take_screenshot_current_window(self.SCREENSHOT_DIR_PATH + "/%s" % filename)
        browser.quit()
