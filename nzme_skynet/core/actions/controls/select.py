# coding=utf-8
from selenium.webdriver.support.select import Select

from nzme_skynet.core.actions.controls.component import Component


class SelectElem(Component):
    def __init__(self, driver, by_locator):
        super(SelectElem, self).__init__(driver, by_locator)
        self.select = self._select_init()

    def _select_init(self):
        return Select(self.find_element())

    def select_by_index(self, index):
        self.select.select_by_index(index)

    def deselect_by_index(self, index):
        self.select.deselect_by_index(index)

    def select_by_value(self, value):
        self.select.select_by_value(value)

    def get_selected_value(self):
        return self.select.first_selected_option

    def get_selected_text(self):
        return self.select.first_selected_option.text

    def get_all_options(self):
        return self.select.options

    def get_options_count(self):
        return len(self.select.options)

