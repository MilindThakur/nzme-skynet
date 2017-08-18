from appium.webdriver.common.mobileby import MobileBy
import requests
from selenium.common.exceptions import NoSuchElementException
import logging

class HomePage(object):
    def __init__(self, app):
        self.logger = logging.getLogger(__name__)
        self.app = app

        #IWebElements

        self.homepageMessageBox = self.app