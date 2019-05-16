# coding=utf-8
from selenium.webdriver.support.select import Select

from nzme_skynet.core.controls.baseelement import BaseElement


class SelectElem(BaseElement):

    def __init__(self, by, locator):
        super(SelectElem, self).__init__(by, locator)
        self.select = None

    def _select_init(self):
        try:
            self.select = Select(self._find_element())
        except Exception:
            pass

    def select_by_index(self, index):
        self._select_init()
        self._highlight()
        self.select.select_by_index(index)

    def deselect_by_index(self, index):
        self._select_init()
        self._highlight()
        self.select.deselect_by_index(index)

    def select_by_value(self, value):
        self._select_init()
        self._highlight()
        self.select.select_by_value(value)

    def get_selected_value(self):
        self._select_init()
        self._highlight()
        return self.select.first_selected_option

    def get_selected_text(self):
        self._select_init()
        self._highlight()
        return self.select.first_selected_option.text

    def get_all_options(self):
        self._select_init()
        self._highlight()
        return self.select.options

    def get_options_count(self):
        self._select_init()
        return len(self.select.options)
