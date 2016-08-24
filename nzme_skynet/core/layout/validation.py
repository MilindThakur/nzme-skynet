# coding=utf-8
import json
import os
from datetime import datetime
import requests
from nzme_skynet.core.browsers.localbrowserbuilder import LocalBrowserBuilder

class Validation(object):
    _CUR_DIR = os.path.dirname(__file__)
    _DEFAULT_PATH = os.path.abspath('.') + "/PageValidationResults"
    _DEFAULT_FILENAME = "%s_%s.txt" % ("pagevalidation_results", datetime.now().strftime("%Y%m%d-%H%M%S"))

    def __init__(self, urls_path, custom_results_path=None):
        with open(urls_path, 'r') as urlf:
            self.urls_json = json.load(urlf)
        lb = LocalBrowserBuilder("phantomJS")
        browser = lb.build()
        self.mydriver = browser.driver
        if custom_results_path:
            self._results_path = custom_results_path
        else:
            self._results_path = self._DEFAULT_PATH

    def validate(self):
        invalid_result = {}
        invalid_links = invalid_images = []
        for url in self.urls_json["urls"]:
            self.mydriver.get(url["url"])
            invalid_images = self._validate_images_on_url()
            invalid_links = self._validate_links_on_url()
        if invalid_links + invalid_images:
            invalid_result[url["url"]] = invalid_links + invalid_images
            self._create_folder_and_write_result_to_file(self._results_path, invalid_result)

    def _create_results_folder(self, folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def _validate_images_on_url(self):
        images = self.mydriver.find_elements_by_tag_name("img")
        broken_images_list = []
        for image in images:
            b = self.mydriver.execute_script("return arguments[0].complete && "
                                             "typeof arguments[0].naturalWidth != \"undefined\" && "
                                             "arguments[0].naturalWidth > 0", image)
            if not b:
                broken_images_list.append(image.get_attribute("src"))
        return broken_images_list

    def _validate_links_on_url(self):
        links = self.mydriver.find_elements_by_xpath("//a[@href]")
        broken_links_list = []
        for link in links:
            if link.is_displayed() and ("http" in link.get_attribute("href")):
                if not self._is_link_broken(link.get_attribute("href")):
                    broken_links_list.append(link.text)
        return broken_links_list

    def _is_link_broken(self, link):
        return requests.get(link).status_code == 200

    def _create_folder_and_write_result_to_file(self, folder, result):
        self._create_results_folder(folder)
        result_file = (self._results_path + "/%s" % self._DEFAULT_FILENAME)
        target = open(result_file, 'w')
        #target.write(str(result))
        for i in result.keys():
            target.write(repr(i))
            for n in result[i]:
                target.write(' %s'%(repr(n)))
            target.write('\n')
        target.close()
