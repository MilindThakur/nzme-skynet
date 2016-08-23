# coding=utf-8

class Text(object):
    def __init__(self, by_locator):
        self.locator = by_locator

    def get_text(self):
        pass

    def text_contains(self, text):
        pass

    def text_matches(self, regex):
        pass