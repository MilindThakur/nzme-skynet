# coding=utf-8
import json
import os
from datetime import datetime

from nzme_skynet.core.browsers.localbrowserbuilder import LocalBrowserBuilder


class LayoutScreenshot(object):
    _SCREENSHOT_DIR_NAME = "screenshot"
    _SCREENSHOT_DIR_PATH = os.path.abspath('.') + "/%s" % _SCREENSHOT_DIR_NAME

    def __init__(self, urls_path, device_list=None, folder=None):
        with open(urls_path, 'r') as url:
            self.urls_json = json.load(url)
        with open(os.path.dirname(__file__) + "/devices.json", 'r') as devices:
            self.devices_json = json.load(devices)
        if device_list:
            self._devices_list = device_list.split(',')
        else:
            self._devices_list = list(self.devices_json.keys())
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
            browser.goto_url(url["url"])
            for device in self._devices_list:
                browser.set_window_size(self.devices_json[device]["w"], self.devices_json[device]["h"])
                filename = "%s_%s_%s.png" % (url["name"].replace(" ", ""), device,
                                             datetime.now().strftime("%Y%m%d-%H%M%S"))
                browser.take_screenshot_current_window(self._folder + "/%s" % filename)
        browser.quit()
