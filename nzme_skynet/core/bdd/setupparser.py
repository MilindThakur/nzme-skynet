# coding=utf-8
import ConfigParser
import logging
import os


def get_browser_options(config):
    browser_local_options = {'type': config.get('BROWSER', 'type'),
                             'version': config.get('BROWSER', 'version'),
                             'os': config.get('BROWSER', 'os'),
                             'windowwidth': config.get('BROWSER', 'windowwidth'),
                             'windowheight': config.get('BROWSER', 'windowheight'),
                            }
    return browser_local_options


def get_mobile_andorid_options(config):
    mobile_local_options = {'platform': config.get('ANDROID', 'platform'),
                            'selenium_grid_hub': config.get('CLOUD', 'selenium_grid_hub'),
                            'platformVersion': config.get('ANDROID', 'platformVersion'),
                            'version': config.get('ANDROID', 'version'),
                            'platformName': config.get('ANDROID', 'platformName'),
                            'deviceName': config.get('ANDROID', 'deviceName'),
                            'app': config.get('ANDROID', 'app'),
                            'appPackage': config.get('ANDROID', 'appPackage'),
                            'appActivity': config.get('ANDROID', 'appActivity'),
                            'fullReset': config.get('ANDROID', 'fullReset'),
                            'clearSystemFiles': config.get('ANDROID', 'clearSystemFiles'),
                            'newCommandTimeout':'newCommandTimeout=120'
                            }
    return mobile_local_options


def get_mobile_ios_options(config):
    mobile_local_options = {'platform': config.get('IOS', 'platform'),
                            'selenium_grid_hub': config.get('CLOUD', 'selenium_grid_hub'),
                            'platformName': config.get('IOS', 'platformName'),
                            'platformVersion': config.get('IOS', 'platformVersion'),
                            'deviceName': config.get('IOS', 'deviceName'),
                            'app': config.get('IOS', 'app'),
                            'bundleId': config.get('IOS', 'bundleId'),
                            'appActivity': config.get('IOS', 'appActivity'),
                            'fullReset': config.get('IOS', 'fullReset')
                            }
    return mobile_local_options


def get_android_chrome_options(config):
    mobile_local_options = {
                            'selenium_grid_hub': config.get('CLOUD', 'selenium_grid_hub'),
                            'platform': config.get('ANDROID', 'platform'),
                            'platformName': config.get('ANDROID', 'platformName'),
                            'deviceName': config.get('ANDROID', 'deviceName'),
                            'browserName': config.get('ANDROID_CHROME', 'browser'),
                            'version': config.get('ANDROID', 'version'),
                            "chromeOptions": {'args': [config.get('ANDROID_CHROME', 'chromeoptions')]}
                            }
    return mobile_local_options


class Config(object):
    config = ConfigParser.SafeConfigParser(allow_no_value=True)
    config.read('testsetup.ini')
    logger = logging.getLogger(__name__)

    BROWSER_OPTIONS = get_browser_options(config)
    if not BROWSER_OPTIONS['type']:
        logger.warning("Setting Chrome as the default browser")
        BROWSER_OPTIONS['type'] = 'chrome'

    # TODO - build up mobile options.
    MOBILE_ANDROID_OPTIONS = get_mobile_andorid_options(config)
    MOBILE_IOS_OPTIONS = get_mobile_ios_options(config)
    ANDROID_CHROME_OPTIONS = get_android_chrome_options(config)

    ENV_BASE_URL = config.get('ENVIRONMENT', 'baseurl')
    ENV_IS_LOCAL = config.getboolean('ENVIRONMENT', 'local')

    SEL_GRID_URL = config.get('CLOUD', 'selenium_grid_hub')
    LOG = os.path.abspath('logs')

