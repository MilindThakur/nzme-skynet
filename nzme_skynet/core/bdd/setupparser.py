# coding=utf-8
import ConfigParser
import os
import logging


class Config(object):
    config = ConfigParser.SafeConfigParser()
    config.read('testsetup.ini')
    logger = logging.getLogger(__name__)

    BROWSER_NAME = config.get('BROWSER', 'type')
    if not BROWSER_NAME:
        logger.error("Please specify the browser name: chrome, firefox etc")
        raise Exception("Please specify the browser name: chrome, firefox etc")
    BROWSER_OS = config.get('BROWSER', 'os')
    BROWSER_VERSION = config.get('BROWSER', 'version')

    ENV_BASE_URL = config.get('ENVIRONMENT', 'baseurl')
    ENV_IS_LOCAL = config.getboolean('ENVIRONMENT', 'local')

    SEL_GRID_URL = config.get('CLOUD', 'selenium_grid_hub')
    LOG = os.path.abspath('logs')
