# coding=utf-8
from nzme_skynet.core.mobile.mobileapp import MobileApp


class AndroidDriver(MobileApp):

    def __init__(self, desired_caps):
        super(AndroidDriver, self).__init__(desired_caps)
