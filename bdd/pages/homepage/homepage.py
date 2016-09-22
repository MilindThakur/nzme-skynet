# coding=utf-8
from selenium.webdriver.common.by import By

from bdd.pages.homepage.registerform import RegisterForm


class HomePage(object):

    def __init__(self, app):
        self.app = app
        self.register_txtlnk = self.app.get_actions().textlink(By.LINK_TEXT, "Register")
        self.profile_lnk = self.app.get_actions().textlink(By.ID, "ubProfile")
        self.register_form_page = None

    def open_register_form(self):
        self.register_txtlnk.click()

    def get_registration_form(self):
        if self.register_form_page is None:
            return RegisterForm(self.app)
        return self.register_form_page
