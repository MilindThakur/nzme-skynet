# coding=utf-8
import ConfigParser
import logging
import os


def get_browser_options(config):
    browser_local_options = {'type': config.get('BROWSER', 'type'),
                             'version': config.get('BROWSER', 'version'),
                             'os': config.get('BROWSER', 'os'),
                             'windowwidth': config.get('BROWSER', 'windowwidth'),
                             'windowheight': config.get('BROWSER', 'windowheight')
                             }
    return browser_local_options


class Config(object):
    config = ConfigParser.SafeConfigParser(allow_no_value=True)
    config.read('testsetup.ini')
    logger = logging.getLogger(__name__)

    BROWSER_OPTIONS = get_browser_options(config)
    if not BROWSER_OPTIONS['type']:
        logger.warning("Setting Chrome as the default browser")
        BROWSER_OPTIONS['type'] = 'chrome'

    ENV_BASE_URL = config.get('ENVIRONMENT', 'baseurl')
    ENV_IS_LOCAL = config.getboolean('ENVIRONMENT', 'local')

    SEL_GRID_URL = config.get('CLOUD', 'selenium_grid_hub')
    LOG = os.path.abspath('logs')
