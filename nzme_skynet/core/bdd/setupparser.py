# coding=utf-8
import ConfigParser
import os


def create_desktop_browser_capabilities(config):
    desired_capabilities = {'browserName': config.get('BROWSER', 'type'),
                            'platform': config.get('BROWSER', 'os'),
                            'version': '' if 'latest' in config.get('BROWSER', 'version') else
                            config.get('BROWSER', 'version'),
                            'highlight': config.getboolean('BROWSER', 'highlight')
                            }
    return desired_capabilities


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

    DESKTOP_BROWSER_CAPABILITIES = create_desktop_browser_capabilities(config)

    ANDROID_CAPABILITIES = dict(config.items('ANDROID'))

    IOS_CAPABILITIES = dict(config.items('IOS'))

    ENV_OPTIONS = get_environment_options(config)

    LOG = os.path.abspath('logs')

