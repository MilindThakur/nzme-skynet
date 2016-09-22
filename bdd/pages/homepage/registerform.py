# coding=utf-8
from selenium.webdriver.common.by import By

class RegisterForm(object):

    def __init__(self, app):
        self.app = app
        self.firstname_input = self.app.get_actions().textinput(By.ID, "default_first_name")
        self.lastname_input = self.app.get_action().textinput(By.ID, "default_last_name")
        self.email_input = self.app.get_actions().textinput(By.ID, "default_email")
        self.confirm_email_input = self.app.get_actions().textinput(By.ID, "default_email_confirm")
        self.password = self.app.get_actions().textinput(By.ID, "default_password")
        self.birthyear_dropdown = self.app.get_actions().selectlist(By.ID, "default_dob_year")
        self.postcode_input = self.app.get_actions().textinput(By.ID, "default_postcode")
        self.male_btn = self.app.get_actions().radiobutton(By.XPATH, "//label[@for='default_gender_Male']")
        self.female_btn = self.app.get_actions().radiobutton(By.XPATH, "//label[@for='default_gender_Female']")
        self.select_offer_chk = self.app.get_actions().checkbox(By.XPATH, "//label[@for='default_promo']")
        self.register_button = self.app.get_actions().button(By.XPATH, "//input[@value='Register Me']")

        self.last_page_form = self.app.get_actions().elem(By.CLASS_NAME, "lastPageForm")
        self.form_cancel_button = self.app.get_actions().button(By.CLASS_NAME, "fancyCloseCustom")

    def fill_form(self, user):
        self.firstname_input.will_be_displayed()
        self.firstname_input.set_value(user.firstname)
        self.lastname_input.set_value(user.lastname)
        self.email_input.set_value(user.email)
        self.confirm_email_input.set_value(user.email)
        self.password.set_value(user.password)
        self.birthyear_dropdown.select_by_value(user.birthyear)
        self.postcode_input.set_value(user.postcode)
        if user.gender == "M":
            self.male_btn.click()
        if user.gender == "F":
            self.female_btn.click()
        self.select_offer_chk.uncheck()

    def submit_register_form(self):
        self.register_button.will_be_displayed()
        self.register_button.click()