# coding=utf-8
from nzme_skynet.core.actions.controls.component import Component


class TextLink(Component):
    def __index__(self, driver, by_locator):
        super(TextLink, self).__init__(driver, by_locator)

    def get_href(self):
        self.get_attribute("href")
