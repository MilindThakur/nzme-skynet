# coding=utf-8
from appium import webdriver


class IosDriver(object):
    def __init__(self, desired_caps):
        self.base_url = desired_caps['appium_url']
        self.desired_caps = desired_caps
        self.driver = None

    '''
        def get_default_desiredcapabilities(self):
            chrome_options = Options()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--test-type")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("-process-per-site")
            chrome_options.add_argument("--dns-prefetch-disable")
            return chrome_options
    '''

    def _create_webdriver(self):
        try:
            # TODO - returns a session?
            return webdriver.Remote(self.base_url,self.desired_caps)
        except Exception:
            raise
