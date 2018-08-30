# coding=utf-8
import ConfigParser
import os


def get_environment_options(config):
    return {
            'testurl': config.get('ENVIRONMENT', 'testurl'),
            'local': config.getboolean('ENVIRONMENT', 'local'),
            'selenium_grid_hub': config.get('ENVIRONMENT', 'selenium_grid_hub'),
            'zalenium': config.getboolean('ENVIRONMENT', 'zalenium')
    }


class Config(object):
    config = ConfigParser.SafeConfigParser(allow_no_value=True)
    # Preserve string case from INI for capability matching
    config.optionxform = str
    config.read('testsetup.ini')

    BROWSER_CAPABILITIES = dict(config.items('BROWSER'))

    ANDROID_CAPABILITIES = dict(config.items('ANDROID'))

    IOS_CAPABILITIES = dict(config.items('IOS'))

    ENV_OPTIONS = get_environment_options(config)

    LOG = os.path.abspath('logs')

