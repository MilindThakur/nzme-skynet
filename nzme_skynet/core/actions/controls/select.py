# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from nzme_skynet.core.actions.controls.component import Component


class SelectElem(Component):
    def __init__(self, driver, locator, by=By.CSS_SELECTOR):
        super(SelectElem, self).__init__(driver, locator, by)
        self.select = None
        self._select_init()

    def _select_init(self):
        try:
            self.select = Select(self.find_element())
        except Exception:
            pass

    def select_by_index(self, index):
        self._select_init()
        self.select.select_by_index(index)

    def deselect_by_index(self, index):
        self._select_init()
        self.select.deselect_by_index(index)

    def select_by_value(self, value):
        self._select_init()
        self.select.select_by_value(value)

    def get_selected_value(self):
        self._select_init()
        return self.select.first_selected_option

    def get_selected_text(self):
        self._select_init()
        return self.select.first_selected_option.text

    def get_all_options(self):
        self._select_init()
        return self.select.options

    def get_options_count(self):
        self._select_init()
        return len(self.select.options)

