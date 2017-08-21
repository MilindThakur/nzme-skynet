from selenium.webdriver.common.by import By
import logging


class Homepage(object):
    def __init__(self, app):
        self.app = app
        self.logger = logging.getLogger(__name__)
        self.actions = self.app.get_actions()
        self.title = self.actions.element(By.ID, "HomeMessage")
        self.home_message = self.app.get_actions().element(By.ID, "HomeMessage")


