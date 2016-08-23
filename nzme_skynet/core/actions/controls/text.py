# coding=utf-8
from nzme_skynet.core.actions.component import Component


class Text(Component):
    def __init__(self, by_locator):
        super(Text, self).__init__(by_locator)

    def get_text(self):
        pass

    def text_contains(self, text):
        pass

    def text_matches(self, regex):
        pass
