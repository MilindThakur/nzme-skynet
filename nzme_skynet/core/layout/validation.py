# coding=utf-8
import json
import os
from nzme_skynet.core.browsers.localbrowserbuilder import LocalBrowserBuilder
import requests
from datetime import datetime



class Validation(object):

    def __init__(self, urls_path, results_path=None):

        try:
            with open(urls_path, 'r') as urlf:
                self.urls_json = json.load(urlf)
        except EnvironmentError:
            print "No path defined"

        lb = LocalBrowserBuilder("phantomJS")
        browser = lb.build()
        self.mydriver = browser.driver
        self.results_path = results_path

        if not self.results_path:
            self.path = os.path.abspath('.') + "/Validation"
        else:
            self.path = self.results_path
        self.create_results_file()

    #create results file to output details of broken images or elements
    def create_results_file(self):

        filename = "%s_%s.txt" % ("val_results", datetime.now().strftime("%Y%m%d-%H%M%S"))
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.filepath = (self.path + "/%s" % filename)
        self.target = open(self.filepath, "a")


    #write to file and return filename if image and link results show items in dictionaries else return Pass
    def validate(self):

        newdict = {}
        newdict.update(self.check_image())
        newdict.update(self.check_link())
        if newdict.values() > 0:
            self.target.write(str(newdict))
            return str(self.filepath)
        else:
            return "Pass"


    #check images are not broken and return dictionary list
    def check_image(self):
        self.uidict = {}
        for url in self.urls_json["urls"]:
            self.mydriver.get(url["url"])
            images = self.mydriver.find_elements_by_tag_name("img")
            srclist = []
            for image in images:
                b = self.mydriver.execute_script("return arguments[0].complete && typeof arguments[0].naturalWidth != \"undefined\" && arguments[0].naturalWidth > 0", image)
                if not b:
                    srclist = image.get_attribute("src")
                    self.uidict.setdefault(url["url"],[]).append(srclist)
            return self.uidict


    #check links are displayed and return expected status code
    def check_link(self):
        self.uidict = {}
        for url in self.urls_json["urls"]:
            self.mydriver.get(url["url"])
            links = self.mydriver.find_elements_by_xpath("//a[@href]")
            hreflist = []
            for link in links:
                if link.is_displayed() and ("http" in link.get_attribute("href")):
                    if not self._is_link_broken(link.get_attribute("href")):
                        hreflist.append(link.text)
                        self.uidict.setdefault(url["url"], []).append(hreflist)
            return self.uidict


    #validate link is not broken by verifying response status code
    def _is_link_broken(self, url):
        #print url
        return requests.get(url).status_code == 200
