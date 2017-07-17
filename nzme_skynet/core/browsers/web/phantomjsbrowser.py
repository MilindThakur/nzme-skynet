# coding=utf-8
from selenium.webdriver.phantomjs.webdriver import WebDriver

from nzme_skynet.core.browsers.web.webbrowser import Webbrowser


class PhantomJSBrowser(Webbrowser):
    def __init__(self, baseUrl, **kwargs):
        super(PhantomJSBrowser, self).__init__(baseUrl, **kwargs)

    def get_default_desiredcapabilities(self):
        raise NotImplementedError

    def _create_webdriver(self):
        service_args = ["--ignore-ssl-errors=true",
                        "--ssl-protocol=any",
                        "--web-security=no"
                        ]
        return WebDriver(service_args=service_args)
