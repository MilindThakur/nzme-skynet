# coding=utf-8
import json
import time
import os

from browsermobproxy import Server
from browsermobproxy import Client
from haralyzer import HarParser

from nzme_skynet.core.driver.driverregistry import DriverRegistry
from nzme_skynet.core.driver.enums.drivertypes import DriverTypes
from nzme_skynet.core.driver.basedriver import BaseDriver


class BrowserProxy(object):
    """
    Base class to for Browser Proxy setup
    """

    def __init__(self):
        self._driver = self._server = self._client = None

    @property
    def driver(self):
        # type: () -> BaseDriver
        """
        Exposes the framework driver wrapper for browser/device interactions
        :return: Framework Driver
        """
        return self._driver

    @property
    def client(self):
        # type: () -> Client
        """
        Exposes Browsermobproxy client
        :return:
        """
        return self._client

    @property
    def harparser(self):
        """
        Captures the har and converts to a HarParser object
        :return: HarParser object, a page from har capture
        """
        result_har = json.dumps(self._client.har, ensure_ascii=False)
        har_parser = HarParser(json.loads(result_har))
        return har_parser.pages[0]

    def start(self):
        """
        Start the proxy and browser
        """
        self.start_proxy()
        self.start_browser()

    def start_proxy(self):
        """
        Start the browsermob-proxy
        """
        raise NotImplementedError

    def start_browser(self, headless=False, resolution="maximum", mobileEmulation=""):
        """
        Start the chrome browser instance
        :param bool headless: run browser in headless mode
        :param str resolution: maximum or width * height
        :param str mobileEmulation: chrome emulation mode e.g. iPhone X, Samsung Galaxy S5 etc
        :return: Framework driver wrapper
        """
        raise NotImplementedError

    def stop(self):
        """
        Stop the proxy and browser instance
        """
        raise NotImplementedError

    def stop_browser(self):
        """
        Stop the browser instance
        """
        if DriverRegistry.get_driver():
            DriverRegistry.deregister_driver()
            self._driver = None

    def stop_proxy(self):
        """
        Stop the proxy
        """
        if self._client:
            self._client.close()
            self._client = None
        if self._server:
            self._server.stop()
            self._server = None

    def capture_url_traffic(self, url, wait_time=0):
        """
        Capture the har for a given url
        :param str url: url to capture traffic for
        :param int wait_time: time to wait after the page load
        :return: HarParser object, a page from har capture
        """
        self._client.new_har(options={'captureHeaders': True})
        self._driver.goto_url(url, absolute=True)
        time.sleep(wait_time)
        result_har = json.dumps(self._client.har, ensure_ascii=False)
        har_parser = HarParser(json.loads(result_har))
        return har_parser.pages[0]

    @staticmethod
    def filter_entry_by_matching_url(har_page, url_matcher):
        """
        Static method to match request url, an absolute string match is made
        e.g. bproxy.filter_entry_by_matching_url(har_page, "gstatic.com")
        :param HarParser.page har_page: HarParser page instance
        :param str url_matcher: matching url
        :return: list of matching page entry
        """
        matching_list = []
        for entry in har_page.entries:
            if url_matcher in entry['request']['url']:
                matching_list.append(entry)
        return matching_list


class BrowserProxyLocal(BrowserProxy):
    """
    Starts local browsermob-proxy server and chrome browser to capture the traffic.
    Example:
        bproxy = BrowserProxyLocal(path_to_binary=BROWSER_PROXY_BIN)
        bproxy.start()
    """
    def __init__(self, path_to_binary='browsermob-proxy'):
        """
        Initialises a new Local Browsermobproxy and browser instance
        :param str path_to_binary: Path to the browsermob proxy bin file
        """
        super(BrowserProxyLocal, self).__init__()
        self._bin_path = path_to_binary

    def start_proxy(self):
        """
        Starts the browsermob-proxy locally
        :return: client instance on browsermob-proxy
        """
        try:
            self._server = Server(path=self._bin_path)
        except Exception:
            raise
        self._server.start()
        self._client = self._server.create_proxy({'captureHeaders': True,
                                                  'captureContent': True,
                                                  'captureBinaryContent': True})

    def start_browser(self, headless=False, resolution="maximum", mobileEmulation=""):
        """
        Starts local chrome browser with proxy configured
        :param bool headless: run browser in headless mode
        :param str resolution: maximum or width * height
        :param str mobileEmulation: chrome emulation mode e.g. iPhone X, Samsung Galaxy S5 etc
        :return: Framework driver wrapper
        """
        proxy_server_arg = "--proxy-server={0}".format(self._client.proxy)
        capabilities = {
            "browserName": "chrome",
            "version": "ANY",
            "platform": "ANY",
            "goog:chromeOptions": {
                "args": [proxy_server_arg, '--ignore-certificate-errors', '--test-type'],
                "extensions": [],
                "prefs": {}
            }
        }
        options = {
            "highlight": False,
            "headless": headless,
            "resolution": resolution,
            "mobileEmulation": mobileEmulation
        }
        DriverRegistry.register_driver(DriverTypes.CHROME, capabilities=capabilities, options=options, local=True)
        self._driver = DriverRegistry.get_driver()

    def stop(self):
        """
        Stop local browsermob-proxy and browser instance
        :return:
        """
        self.stop_browser()
        self.start_proxy()


class BrowserProxyGrid(BrowserProxy):
    """
    Run browsermob-proxy and browser instance in docker mode first. Use to capture and
    analyse traffic. Useful for a CI setup
    Please refer to https://hub.docker.com/r/qautomatron/docker-browsermob-proxy/
    Example:
        capabilities = {
                "browserName": "chrome",
                "platform": 'LINUX',
                "version": '',
                "javascriptEnabled": True
            }
        bproxy = BrowserProxyGrid(capabilities=capabilities)
        bproxy.start()
    """

    def __init__(self, capabilities, grid_url="http://localhost:4444/wd/hub"):
        """
        Initialises Browsermob-proxy grid instance
        :param dict capabilities: Browser/Device capabilities
        :param str grid_url: Selenium grid url
        """
        super(BrowserProxyGrid, self).__init__()
        self._capabilities = capabilities
        self._grid_url = grid_url

    def start_proxy(self):
        """
        Assumes browsermob-proxy is running in a docker container and initiates a client
        :return: browsermob-proxy client instance
        """
        proxy_ip = self._get_browsermobproxy_docker_ip()
        proxy_port = "9090"
        self._client = Client("{0}:{1}".format(proxy_ip, proxy_port))

    @staticmethod
    def _get_browsermobproxy_docker_ip():
        """
        Get the docker IP address of the browsermob-proxy container
        :return: str docker container IP address
        """
        proxy_container = os.popen(
            "docker ps --format {{.Names}} | grep 'proxy'").read().rstrip()
        if not proxy_container:
            raise Exception("Error: Ensure browsermobproxy is running in a docker container")
        network = os.popen(
            "docker inspect --format {{.HostConfig.NetworkMode}} %s" % proxy_container).read().rstrip()
        return os.popen("docker inspect --format {{.NetworkSettings.Networks.%s.IPAddress}} %s" %
                        (network, proxy_container)).read().rstrip()

    def start_browser(self, headless=False, resolution="maximum", mobileEmulation=""):
        """
        Start the browser in a grid with proxy setup
        :param bool headless: run browser in headless mode
        :param str resolution: maximum or width * height
        :param str mobileEmulation: chrome emulation mode e.g. iPhone X, Samsung Galaxy S5 etc
        :return: Framework driver wrapper
        """
        proxy_server_arg = "--proxy-server={0}".format(self._client.proxy)
        options = {
            "highlight": False,
            "headless": headless,
            "resolution": resolution,
            "mobileEmulation": mobileEmulation
        }
        self._capabilities["goog:chromeOptions"] = {
            "args": [proxy_server_arg, '--ignore-certificate-errors', '--test-type']}
        DriverRegistry.register_driver(DriverTypes.CHROME, capabilities=self._capabilities, local=False,
                                       options=options,
                                       grid_url=self._grid_url)
        self._driver = DriverRegistry.get_driver()

    def stop(self):
        """
        Stop the browsermob-proxy and browser instance
        """
        self.stop_browser()
        # TODO: Adding a sleep, otherwise getting a "Unable to close channel." error from Browsermobproxy container.
        time.sleep(5)
        self.stop_proxy()
