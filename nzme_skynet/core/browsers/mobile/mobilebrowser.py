# coding=utf-8
from selenium.webdriver.remote.webdriver import WebDriver

from nzme_skynet.core.actions.uiactionsfactory import UIActionsFactory
from nzme_skynet.core.browsers.browser import Browser


class MobileBrowser(Browser):
    """
    Requires Appium to be running in either iPhone or Android
    simulator mode with settings matching desired capabilities.
    """
    _appium_cmd_executor = "http://0.0.0.1:4723/wd/hub"

    def __init__(self, des_cap, base_url):
        super(MobileBrowser, self).__init__(base_url)
        self.des_cap = des_cap
        self.driver = None

    def quit(self):
        pass

    def get_actions(self):
        return UIActionsFactory.create_ui_action("UIActionsMob", self.driver)

    def get_default_desiredcapabilities(self):
        pass

    def get_browser_type(self):
        return self.des_cap['device']

    def init_browser(self):
        # TODO: Check if Appium is running else set it in the required mode
        self.driver = self._create_webdriver()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        if self.baseUrl is not None:
            self.goto_url(self.baseUrl)

    def _create_webdriver(self):
        return WebDriver(self._appium_cmd_executor, self.des_cap)

    def goto_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url
