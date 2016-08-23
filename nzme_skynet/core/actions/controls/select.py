# coding=utf-8
from nzme_skynet.core.actions.component import Component


class Select(Component):
    def __init__(self, by_locator):
        super(Select, self).__init__(by_locator)

    def select_by_index(self, index):
        pass

    def select_by_value(self, value):
        pass

    def get_selected_value(self):
        pass

    def get_selected_text(self):
        pass

    def get_options(self):
        pass

    def get_options_count(self):
        pass

    def contains_options(self, option):
        pass
