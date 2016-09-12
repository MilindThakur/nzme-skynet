# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component


class Text(Component):
    def __init__(self, driver, by_locator):
        super(Text, self).__init__(driver, by_locator)

    def get_text(self):
        pass

    def text_contains(self, text):
        pass

    def text_matches(self, regex):
        pass
