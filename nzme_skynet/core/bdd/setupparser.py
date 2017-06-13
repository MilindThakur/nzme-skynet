# coding=utf-8
import ConfigParser
import os


class Config(object):

    config = ConfigParser.SafeConfigParser()
    config.read('testsetup.ini')

    BROWSER_NAME = config.get('BROWSER', 'type')
    BROWSER_OS = config.get('BROWSER', 'os')
    BROWSER_VERSION = config.get('BROWSER', 'version')

    ENV_BASE_URL = config.get('ENVIRONMENT', 'baseurl')
    ENV_IS_LOCAL = config.getboolean('ENVIRONMENT', 'local')

    SEL_GRID_URL = config.get('CLOUD', 'selenium_grid_hub')
    LOG = os.path.abspath('logs')