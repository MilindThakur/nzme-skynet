# coding=utf-8
import json
import os

from browsermobproxy import Server
from browsermobproxy import Client
from haralyzer import HarParser
from selenium import webdriver


class BrowserProxy(object):
    """
    Create HTTP Archive (har) file using browsermob-proxy. Useful for watching
    and manipulating network traffic originating from the browser.
    """

    def __init__(self, path_to_browsermobproxy_bin=None, local_run=True, grid_url="http://localhost:4444/wd/hub"):
        self._bin_path = path_to_browsermobproxy_bin if path_to_browsermobproxy_bin else 'browsermob-proxy'
        self._server = self._driver = self._proxy = None
        self.local_run = local_run
        self._grid_url = grid_url

    @property
    def driver(self):
        return self._driver

    def start(self):
        if self.local_run:
            self._start_local_server_proxy()
            self._create_local_browser_driver()
        else:
            self._start_grid_proxy()
            self._create_grid_browser_driver()

    def _start_local_server_proxy(self):
        try:
            self._server = Server(path=self._bin_path)
        except Exception:
            raise Exception("Error: Ensure the browsermob-proxy is added to the PATH if no path provided")
        self._server.start()
        self._proxy = self._server.create_proxy({'captureHeaders': True,
                                                 'captureContent': True,
                                                 'captureBinaryContent': True})

    def _start_grid_proxy(self):
        browsermobproxy_ip = self._get_browsermobproxy_docker_ip()
        proxy_port = "9090"
        self._proxy = Client("{0}:{1}".format(browsermobproxy_ip, proxy_port))

    @staticmethod
    def _get_browsermobproxy_docker_ip():
        proxy_container = os.popen("docker ps --format {{.Names}} | grep 'proxy'").read().rstrip()
        if not proxy_container:
            raise Exception("Please run the docker-compose.sh to start the grid with browsermobproxy "
                            "and then try again.")
        network = os.popen("docker inspect --format {{.HostConfig.NetworkMode}} %s" % proxy_container).read().rstrip()
        return os.popen("docker inspect --format {{.NetworkSettings.Networks.%s.IPAddress}} %s" %
                        (network, proxy_container)).read().rstrip()

    def _create_local_browser_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--proxy-server={0}".format(self._proxy.proxy))
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--test-type')
        chrome_options.add_argument('--headless')
        self._driver = webdriver.Chrome(chrome_options=chrome_options)

    def _create_grid_browser_driver(self):
        webdriver_proxy = self._proxy.webdriver_proxy()
        cap = {
            "browserName": "chrome",
            "platform": 'LINUX',
            "version": '',
            "javascriptEnabled": True
            }
        self._driver = webdriver.Remote(command_executor=self._grid_url,
                                        desired_capabilities=cap,
                                        proxy=webdriver_proxy)

    @staticmethod
    def _write_to_file(filename, data):
        with open(filename + '.har', 'w') as f:
            f.write(data)

    def create_har_page(self, url, filename):
        """
        Capture web traffic in a har file and provide a HarPage handler for analysis
        :param url: url to proxy
        :param filename: HAR filename
        :return: instance of HarPage
        """
        self.init_har(filename)
        self._driver.get(url)
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

    def _stop_server(self):
        if self._proxy:
            self._proxy.close()
        if self._server:
            self._server.stop()

    def _stop_driver(self):
        if self._driver:
            self._driver.quit()

    def stop(self):
        self._stop_server()
        self._stop_driver()
