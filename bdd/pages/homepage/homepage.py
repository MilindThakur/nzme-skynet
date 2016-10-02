# coding=utf-8
from selenium.webdriver.common.by import By

from bdd.pages.homepage.registerform import RegisterForm


class HomePage(object):

    def __init__(self, app):
        self.app = app
        self.register_txtlnk = self.app.get_actions().textlink(By.ID, "ubRegister")
        self.profile_lnk = self.app.get_actions().textlink(By.ID, "ubProfile")
        self._register_form_page = None

    def open_register_form(self):
        self.register_txtlnk.click()

    @property
    def registration_form_page(self):
        if self._register_form_page is None:
            self._register_form_page = RegisterForm(self.app)
        return self._register_form_page
