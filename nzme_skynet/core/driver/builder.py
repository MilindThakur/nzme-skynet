# coding=utf-8
import logging

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from nzme_skynet.core.driver.web.builder.localbrowserbuilder import LocalBrowserBuilder
from nzme_skynet.core.driver.web.builder.remotebrowserbuilder import RemoteBrowserBuilder
from nzme_skynet.core.driver.mobile.builder.appiumdriverbuilder import AppiumDriverBuilder
from nzme_skynet.core.driver.web.browsers.webbrowser import Webbrowser
from nzme_skynet.core.driver.web.browsers.remotebrowser import RemoteBrowser

CAPABILITIES = {"firefox": DesiredCapabilities.FIREFOX,
                "chrome": DesiredCapabilities.CHROME,
                "safari": DesiredCapabilities.SAFARI,
                "ie": DesiredCapabilities.INTERNETEXPLORER,
                "opera": DesiredCapabilities.OPERA,
                "phantomjs": DesiredCapabilities.PHANTOMJS,
                "iphone": DesiredCapabilities.IPHONE,
                "ipad": DesiredCapabilities.IPAD,
                "android": DesiredCapabilities.ANDROID}

logger = logging.getLogger(__name__)


# TODO - convert this to  Driver factory?
# Browser
def build_desktop_browser(browser_options, base_url=None):
    # type: () -> Webbrowser
    logger.debug("Creating local browser instance")
    builder = LocalBrowserBuilder(browser_options, base_url)
    return builder.build()


# Docker
def build_docker_browser(sel_grid_url, desired_cap, base_url=None):
    # type: () -> RemoteBrowser
    logger.debug("Creating a browser instance using selenium-grid")
    desired_cap['javascriptEnabled'] = True
    builder = RemoteBrowserBuilder(sel_grid_url, desired_capabilities=desired_cap,
                                   base_url=base_url)
    return builder.build()


def build_mobile_browser(desired_cap, test_url=None):
    driver = AppiumDriverBuilder(desired_cap).build()
    # need to accept terms and conditions if displayed.
    if test_url is not None:
        driver.goto_url(test_url, relative=False)
    return driver


def build_simulator_mobile_browser():
    raise NotImplementedError


def build_appium_driver(desired_cap):
    logger.debug("Creating Appium driver for: " + desired_cap['platform'])
    return AppiumDriverBuilder(desired_cap).build()




