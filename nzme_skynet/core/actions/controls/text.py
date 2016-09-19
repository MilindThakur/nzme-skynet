# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component


class Text(Component):
    def __init__(self, driver, by_locator):
        super(Text, self).__init__(driver, by_locator)

    def get_text(self):
        self.get_text()

    def text_contains(self, text):
        return self.get_text().contains(text)

    def text_matches(self, regex):
        return self.get_text().matches(regex)
