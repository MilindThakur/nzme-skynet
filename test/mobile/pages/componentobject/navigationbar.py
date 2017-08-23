from selenium.webdriver.common.by import By

class NavigationBar(object):
    def __init__(self, app):
        self.app = app
        self.bar = self.app.get_actions().mobelement(By.ID,"navigation")
        self.navigation_cell = self.app.get_actions().mobelement(By.ID, "navigation")