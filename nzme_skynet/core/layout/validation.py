# coding=utf-8
import json
import os
import requests

from datetime import datetime
from nzme_skynet.core.browsers.localbrowserbuilder import LocalBrowserBuilder
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Validation(object):
    _DEFAULT_PATH = os.path.abspath('./') + "/ValidationResults"
    _DEFAULT_FILENAME = "%s_%s.txt" % ("pagevalidation_results", datetime.now().strftime("%Y%m%d-%H%M%S"))


    def __init__(self, urls_path, custom_results_path=None):
        with open(urls_path, 'r') as urlf:
            self.urls_json = json.load(urlf)
        capabilities = DesiredCapabilities.PHANTOMJS
        capabilities['loggingPrefs'] = {'browser': 'ALL'}
        lb = LocalBrowserBuilder("phantomJS", desCap=capabilities)
        browser = lb.build()
        self.mydriver = browser.driver
        if custom_results_path:
            self._results_path = custom_results_path
        else:
            self._results_path = self._DEFAULT_PATH

    def validateall(self):
        invalid_result = {}
        invalid_links = []
        invalid_images = []
        invalid_js = []
        for url in self.urls_json["urls"]:
            self.mydriver.get(url["url"])
            invalid_images = self.validate_images_on_url()
            invalid_links = self.validate_links_on_url()
            invalid_js = self.validate_javascript_on_url()
        if invalid_links + invalid_images + invalid_js:
            invalid_result[url["url"]] = invalid_links + invalid_images + invalid_js
            self._create_folder_and_write_result_to_file(self._results_path, invalid_result)

    def _create_results_folder(self, folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def validate_images_on_url(self):
        for url in self.urls_json["urls"]:
            self.mydriver.get(url["url"])
            images = self.mydriver.find_elements_by_tag_name("img")
            broken_images_list = []
            for image in images:
                b = self.mydriver.execute_script("return arguments[0].complete && "
                                                 "typeof arguments[0].naturalWidth != \"undefined\" && "
                                                 "arguments[0].naturalWidth > 0", image)
                if not b:
                    broken_images_list.append(image.get_attribute("src"))
        return broken_images_list

    def validate_links_on_url(self):
        for url in self.urls_json["urls"]:
            self.mydriver.get(url["url"])
            links = self.mydriver.find_elements_by_xpath("//a[@href]")
            broken_links_list = []
            for link in links:
                if link.is_displayed() and ("http" in link.get_attribute("href")):
                    if not self._is_link_broken(link.get_attribute("href")):
                        broken_links_list.append(link.text)
        return broken_links_list

    def validate_javascript_on_url(self):
        broken_js_list = []
        log_level = ['WARNING', 'SEVERE', 'FATAL', 'ERROR']
        for url in self.urls_json["urls"]:
            self.mydriver.get(url["url"])
            errors = self.mydriver.get_log('browser')
            for entry in errors:
                if entry['level'] in log_level:
                    broken_js_list.append(str(entry['level'] + ": " + entry['message']))
        return broken_js_list

    def _is_link_broken(self, link):
        return requests.get(link).status_code == 200

    def _create_folder_and_write_result_to_file(self, folder, result):
        self._create_results_folder(folder)
        result_file = (self._results_path + "/%s" % self._DEFAULT_FILENAME)
        target = open(result_file, 'w')
        for i in result.keys():
            target.write(repr(i))
            target.write('\n')
            for n in result[i]:
                target.write(' %s'%(repr(str(n))))
                target.write('\n')
            target.write('\n' * 2)
        target.close()


