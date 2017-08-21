# coding=utf-8
from appium import webdriver
from nzme_skynet.core.browsers.mobileapp import MobileApp
from nzme_skynet.core.actions.uiactionsmob import UIActionsMob


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
