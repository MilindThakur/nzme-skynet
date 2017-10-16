# coding=utf-8
import ConfigParser
import logging
import os


def create_desktop_browser_capabilities(config):
    desired_capabilities = {'browserName': config.get('BROWSER', 'type'),
                            'platform': config.get('BROWSER', 'os'),
                            'version': config.get('BROWSER', 'version')
                            }
    return desired_capabilities


def create_android_browser_capabilities(config):
    desired_capabilities = {'browserName': config.get('ANDROID', 'androidbrowsername'),
                            'platformVersion': config.get('ANDROID', 'platformVersion'),
                            'deviceName': config.get('ANDROID', 'deviceName')
                            }
    return desired_capabilities


def create_android_app_capabilities(config):
    desired_capabilities = {'platformVersion': config.get('ANDROID', 'platformVersion'),
                            'deviceName': config.get('ANDROID', 'deviceName'),
                            'app': config.get('ANDROID', 'app'),
                            'appPackage': config.get('ANDROID', 'appPackage'),
                            'appActivity': config.get('ANDOIRD', 'appActivity')
                            }
    return desired_capabilities


def create_ios_browser_capabilities(config):
    desired_capabilities = {'browserName': config.get('IOS', 'iosbrowsername'),
                            'platformVersion': config.get('IOS', 'platformVersion'),
                            'deviceName': config.get('IOS', 'deviceName')
                            }
    return desired_capabilities


def create_ios_app_capabilities(config):
    desired_capabilities = {'platformVersion': config.get('IOS', 'platformVersion'),
                            'deviceName': config.get('IOS', 'deviceName'),
                            'app': config.get('IOS', 'app'),
                            'bundleId': config.get('IOS', 'bundleId'),
                            'appActivity': config.get('IOS', 'appActivity')
                            }
    return desired_capabilities


def get_environment_options(config):
    return {
            'test_url': config.get('ENVIRONMENT', 'test_url'),
            'local_run': config.getboolean('ENVIRONMENT', 'local_run'),
            'grid_url': config.get('ENVIRONMENT', 'selenium_grid_hub')
    }


class Config(object):
    config = ConfigParser.SafeConfigParser(allow_no_value=True)
    config.read('testsetup.ini')
    logger = logging.getLogger(__name__)

    DESKTOP_BROWSER_CAPABILITIES = create_desktop_browser_capabilities(config)
    ANDROID_APP_CAPABILITIES = create_android_app_capabilities(config)
    ANDROID_BROWSER_CAPABILITIES = create_android_browser_capabilities(config)
    IOS_APP_CAPABILITIES = None
    IOS_BROWSER_CAPABILITIES = create_ios_browser_capabilities(config)

    ENV_OPTIONS = get_environment_options(config)

    LOG = os.path.abspath('logs')

