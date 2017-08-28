# coding=utf-8
import json

from browsermobproxy import Server
from haralyzer import HarParser
from selenium import webdriver


class Har(object):
    """
    Create HTTP Archive (har) file using browsermob-proxy. Useful for watching
    and manipulating network traffic originating from the browser.
    TODO: Support selenium grid, cloud testing
    """

    def __init__(self, path_to_browsermobproxy_bin=None, browser="phantomjs"):
        self.bin_path = path_to_browsermobproxy_bin if path_to_browsermobproxy_bin else 'browsermob-proxy'
        self._browser = browser
        self._server = self._proxy = self.driver = None

    def _start_server(self):
        self._server = Server(self.bin_path)
        self._server.start()
        self._proxy = self._server.create_proxy({'captureHeaders': True,
                                                 'captureContent': True,
                                                 'captureBinaryContent': True})

    def _stop_server(self):
        if self._server:
            self._server.stop()

    def _create_driver(self):
        if self._browser == "phantomjs":
            service_args = ["--proxy=%s" % self._proxy.proxy,
                            "--web-security=no",
                            "--ssl-protocol=any",
                            "--ignore-ssl-errors=yes"]
            self.driver = webdriver.PhantomJS(service_args=service_args)
        if self._browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--proxy-server={0}".format(self._proxy.proxy))
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--test-type')
            self.driver = webdriver.Chrome(chrome_options=chrome_options)

    @staticmethod
    def _write_to_file(filename, data):
        with open(filename + '.har', 'w') as f:
            f.write(data)

    def start(self):
        self._start_server()
        self._create_driver()

    def create_har_page(self, url, filename):
        """
        Capture web traffic in a har file and provide a HarPage handler for analysis
        :param url: url to proxy
        :param filename: HAR filename
        :return: instance of HarPage
        """
        self.init_har(filename)
        self.driver.get(url)
        return self.get_har_page()

    def init_har(self, filename):
        self._proxy.new_har(filename)

    def get_har_page(self):
        result_har = json.dumps(self._proxy.har, ensure_ascii=False)
        har_parser = HarParser(json.loads(result_har))
        return har_parser.pages[0]

    @staticmethod
    def filter_entry_by_matching_url(page, url_matcher):
        matching_list = []
        for entry in page.entries:
            if url_matcher in entry['request']['url']:
                matching_list.append(entry)
        return matching_list

    def _stop_driver(self):
        if self.driver:
            self.driver.quit()

    def stop(self):
        self._stop_server()
        self._stop_driver()
