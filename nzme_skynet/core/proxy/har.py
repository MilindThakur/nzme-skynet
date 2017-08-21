# coding=utf-8
import json

from browsermobproxy import Server
from haralyzer import HarParser
from selenium.webdriver.phantomjs import webdriver


class Har(object):
    """
    Create HTTP Archive (har) file using browsermob-proxy. Useful for watching
    and manipulating network traffic originating from the browser.
    Supports local PhantomJS browser instance only.
    TODO: Support multiple local browsers, selenium grid, cloud testing
    """

    def __init__(self, path_to_browsermobproxy_bin=None):
        self.bin_path = path_to_browsermobproxy_bin if path_to_browsermobproxy_bin else 'browsermob-proxy'
        self.server = self.proxy = self.driver = None

    def _start_server(self):
        self.server = Server(self.bin_path)
        self.server.start()
        self.proxy = self.server.create_proxy({'captureHeaders': True,
                                               'captureContent': True,
                                               'captureBinaryContent': True})

    def _stop_server(self):
        if self.server:
            self.server.stop()

    def _create_driver(self):
        service_args = ["--proxy=%s" % self.proxy.proxy,
                        "--web-security=no",
                        "--ssl-protocol=any",
                        "--ignore-ssl-errors=yes"]
        self.driver = webdriver.WebDriver(service_args=service_args)

    @staticmethod
    def _write_to_file(filename, data):
        with open(filename+'.har', 'w') as f:
            f.write(data)

    def start(self):
        self._start_server()
        self._create_driver()

    def create_har_page(self, url, filename, write_to_file=False):
        """
        Capture web traffic in a har file and provide a HarPage handler for analysis
        :param url: url to proxy
        :param filename: HAR filename
        :param write_to_file: If set, create a .har file on disk
        :return: instance of HarPage
        """
        self.proxy.new_har(filename)
        self.driver.get(url)
        result_har = json.dumps(self.proxy.har, ensure_ascii=False)
        if write_to_file:
            self._write_to_file(filename, result_har)
        har_parser = HarParser(json.loads(result_har))
        return har_parser.pages[0]

    def _stop_driver(self):
        if self.driver:
            self.driver.quit()

    def stop(self):
        self._stop_server()
        self._stop_driver()
