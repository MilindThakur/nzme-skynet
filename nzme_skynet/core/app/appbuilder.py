# coding=utf-8
from nzme_skynet.core.browsers.localbrowserbuilder import LocalBrowserBuilder
from nzme_skynet.core.browsers.remotebrowserbuilder import RemoteBrowserBuilder
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


CAPABILITIES = {"firefox": DesiredCapabilities.FIREFOX,
                "chrome": DesiredCapabilities.CHROME,
                "safari": DesiredCapabilities.SAFARI,
                "ie": DesiredCapabilities.INTERNETEXPLORER,
                "opera": DesiredCapabilities.OPERA,
                "phantomjs": DesiredCapabilities.PHANTOMJS,
                "iphone": DesiredCapabilities.IPHONE,
                "ipad":DesiredCapabilities.IPAD,
                "android": DesiredCapabilities.ANDROID}

# Browser
def build_desktop_browser(browser_type, base_url=None):
    builder = LocalBrowserBuilder(browser_type, base_url)
    return builder.build()

def build_docker_browser(browser_type, base_url=None):
    desired_capabilities = CAPABILITIES[browser_type].copy()
    desired_capabilities['javascriptEnabled'] = True
    builder = RemoteBrowserBuilder(desired_capabilities=desired_capabilities,
                                   base_url=base_url)
    return builder.build()

def build_cloud_browser():
    raise NotImplementedError


def build_real_mobile_browser():
    raise NotImplementedError


def build_simulator_mobile_browser():
    raise NotImplementedError


def build_cloud_mobile_browser():
    raise NotImplementedError


# Mobile App
def build_real_mobile_native_app():
    raise NotImplementedError


def build_simulator_mobile_app():
    raise NotImplementedError


def build_cloud_mobile_app():
    raise NotImplementedError
