import logging
from selenium.webdriver.common.by import By


class GoogleHomePage(object):
    def __init__(self, app):
        self.app = app
        self.logger = logging.getLogger(__name__)

        # WebElements

        self.logo = self.app.get_actions().image(By.ID,"hplogo")
        self.searchbox = self.app.get_actions().textinput(By.ID, "lst-ib")
