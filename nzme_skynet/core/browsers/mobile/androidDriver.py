# coding=utf-8
from appium import webdriver

class AndroidDriver():
    def __init__(self, desired_caps):
        self.base_url = desired_caps['appium_url']
        self.desired_caps = desired_caps
        self.driver = None

    def _create_webdriver(self):
        try:
            # TODO - returns a session?
            return webdriver.Remote(self.base_url, self.desired_caps)
        except Exception:
            raise

    def init_driver(self):
        self.driver = self._create_webdriver()
        # TODO - Is this the best place to install the app? probably not.
        # This will need to be moved if we want to do anything else between getting a session and starting the test
        self.driver.install_app(self.desired_caps['app'])
        self.driver.launch_app()
        # Any other special settings
