from selenium.webdriver.common.by import By
from test.mobile.pages.componentobject.navigationbar import NavigationBar

import logging


class HomePage(object):
    def __init__(self, app):
        self.app = app
        self.logger = logging.getLogger(__name__)

        # IWebElements

        self.title = self.app.get_actions().mobelement("HomeMessage")
        self.home_message = self.app.get_actions().mobelement("HomeMessage")
        self._navigation_bar = None
        self.radiobutton_on = self.app.get_actions().mobelement("radioButton_on")
        self.radiobutton_off = self.app.get_actions().mobelement("radioButton_off")
        self.text_label_test = self.app.get_actions().mobelement("textView_test")
        self.enter_text_test = self.app.get_actions().mobelement("entertext_name_test")
        self.toggleButton_test= self.app.get_actions().mobelement("toggleButton_test")
        self.update_text_button = self.app.get_actions().mobelement("updateTextBoxbutton_test")
        self.checkbox_test = self.app.get_actions().mobelement("checkBox_test")


    @property
    def navigation_bar(self):
        if self._navigation_bar is None:
            self._navigation_bar = NavigationBar(self.app)
        return self._navigation_bar






