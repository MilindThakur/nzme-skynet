# coding=utf-8
import json
import os
from datetime import datetime

from nzme_skynet.core.browsers.localbrowserbuilder import LocalBrowserBuilder


class LayoutScreenshot(object):
    _SCREENSHOT_DIR_NAME = "screenshot"
    _SCREENSHOT_DIR_PATH = os.path.abspath('.') + "/%s" % _SCREENSHOT_DIR_NAME

    def __init__(self, urls_path, devices_path, folder=None):
        with open(urls_path, 'r') as url:
            self.urls_json = json.load(url)
        with open(devices_path, 'r') as devices:
            self.devices_json = json.load(devices)
        if folder:
            self._folder = folder
        else:
            self._folder = self._SCREENSHOT_DIR_PATH
        self._create_screenshot_folder(self._folder)

    def _create_screenshot_folder(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

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
                    browser.take_screenshot_current_window(self._folder + "/%s" % filename)
        browser.quit()
