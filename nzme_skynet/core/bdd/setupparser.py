# coding=utf-8
import ConfigParser
import os

class Config(object):

    config = ConfigParser.SafeConfigParser()
    config.read('testsetup.ini')
    BROWSER = config.get('SETUP', 'browser')
    URL = config.get('SETUP', 'baseurl')
    REUSE = config.getboolean('SETUP', 'reuse')
    CLOUD = config.getboolean('SETUP', 'cloud')
    API = config.getboolean('SETUP', 'api')
    BASEURI = config.get('API', 'baseuri')
    LOG = os.path.abspath('logs')
