# coding=utf-8
from appium import webdriver

from nzme_skynet.core.actions.uiactionsmob import UIActionsMob
from nzme_skynet.core.mobile.mobileapp import MobileApp


class AndroidDriver(MobileApp):
    action_class = UIActionsMob

    def __init__(self, desired_caps):
        super(AndroidDriver, self).__init__(desired_caps)
        self.base_url = desired_caps['appium_url']
        self.desired_caps = desired_caps
        self.driver = None

    def _create_webdriver(self):
        try:
            return webdriver.Remote(self.base_url, self.desired_caps)
        except Exception, e:
            raise

    def get_driver_type(self):
        return self.driver.desired_capabilities['platform']

    def is_app_installed(self):
        return self.driver.is_app_installed(self.desired_caps['appPackage'])
