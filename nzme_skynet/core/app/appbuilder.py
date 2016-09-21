# coding=utf-8
from nzme_skynet.core.browsers.localbrowserbuilder import LocalBrowserBuilder


# Browser
def build_desktop_browser(browser_type, base_url=None):
    builder = LocalBrowserBuilder(browser_type, base_url)
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
